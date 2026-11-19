# Sistema de Controle de Demandas — Full Stack (SQL, Python & Web)

Projeto demonstrativo de aplicação **Full Stack** unindo **modelagem relacional em SQL**, **API REST em Python (Flask)** e **interface web (HTML, CSS e JavaScript)** para registro, precificação estimada e acompanhamento de demandas operacionais.

---

## Arquitetura do Projeto

* **`schema_e_consultas.sql`:** Definição da tabela de demandas, carga inicial de exemplo e consulta agregada por área e status.
* **`app.py`:** API REST com endpoints `GET /api/demandas`, `POST /api/demandas` e `PATCH /api/demandas/<id>/status`, validação de dados e persistência em SQLite.
* **`index.html`:** Interface web para cadastro de novas demandas, visualização tabular e atualização de status em tempo real.

---

## Como Executar Localmente

1. Instale o Flask:
   ```bash
   pip install flask
