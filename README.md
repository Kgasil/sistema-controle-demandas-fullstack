# Sistema de Controle de Demandas — Full Stack (SQL, Python & Web)

Projeto demonstrativo de aplicação **Full Stack** unindo **modelagem relacional em SQL**, **API REST em Python (Flask)** e **interface web (HTML, CSS e JavaScript)** para registro, precificação estimada e acompanhamento de demandas operacionais.
> 🌐 *English version available below:* [Jump to English Version](#english-version)
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
---

<a id="english-version"></a>

# Demand Control System — Full Stack (SQL, Python & Web)[cite: 10]

Demonstrative Full Stack application combining **relational SQL modeling**, a **Python (Flask) REST API**, and a **web interface (HTML, CSS, and JavaScript)** for logging, estimating costs, and tracking operational demands[cite: 10].

## Project Architecture[cite: 10]

* `schema_e_consultas.sql`: Defines the demands table, sample initial seed data, and aggregated queries by department and status[cite: 10].
* `app.py`: REST API featuring `GET /api/demandas`, `POST /api/demandas`, and `PATCH /api/demandas/<id>/status` endpoints, input validation, and SQLite persistence[cite: 10].
* `index.html`: Web interface for creating new demands, viewing tabular records, and updating statuses in real time[cite: 10].

## How to Run Locally[cite: 10]

1. Install Flask[cite: 10]:

```bash
pip install flask
