import sqlite3
import math
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)
DB_NAME = BASE_DIR / "demandas.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS demandas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                area TEXT NOT NULL,
                custo_estimado REAL NOT NULL DEFAULT 0.0,
                status TEXT NOT NULL DEFAULT 'Pendente'
            )
            """
        )
        conn.commit()


@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/api/demandas", methods=["GET"])
def listar_demandas():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM demandas ORDER BY id DESC").fetchall()
        return jsonify([dict(row) for row in rows])


@app.route("/api/demandas", methods=["POST"])
def criar_demanda():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie um objeto JSON válido."}), 400
    titulo = str(dados.get("titulo", "")).strip()
    area = str(dados.get("area", "")).strip()
    status = str(dados.get("status", "Pendente")).strip()

    if status not in {"Pendente", "Em Andamento", "Concluído"}:
        return jsonify({"erro": "Status inválido."}), 400
    if not titulo or not area:
        return jsonify({"erro": "Título e área são obrigatórios."}), 400

    try:
        custo = float(dados.get("custo_estimado", 0))
        if not math.isfinite(custo) or custo < 0:
            raise ValueError()
    except (TypeError, ValueError):
        return jsonify({"erro": "Custo estimado deve ser um número válido."}), 400

    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO demandas (titulo, area, custo_estimado, status) VALUES (?, ?, ?, ?)",
            (titulo, area, custo, status),
        )
        conn.commit()
        novo_id = cursor.lastrowid

    return jsonify({"id": novo_id, "mensagem": "Demanda criada com sucesso."}), 201


@app.route("/api/demandas/<int:demanda_id>/status", methods=["PATCH"])
def atualizar_status(demanda_id):
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie um objeto JSON válido."}), 400
    novo_status = str(dados.get("status", "")).strip()

    if novo_status not in {"Pendente", "Em Andamento", "Concluído"}:
        return jsonify({"erro": "Status inválido."}), 400

    with get_connection() as conn:
        cur = conn.execute(
            "UPDATE demandas SET status = ? WHERE id = ?",
            (novo_status, demanda_id),
        )
        conn.commit()
        if cur.rowcount == 0:
            return jsonify({"erro": "Demanda não encontrada."}), 404

    return jsonify({"mensagem": "Status atualizado."})


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", debug=False, port=5000)
