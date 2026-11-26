# Sistema de Controle de Demandas — Full Stack (SQL, Python & Web)

<!-- kg-personal-portfolio-v1 -->

[KG Professional Portfolio 1.0 — Portfólio pessoal / Personal portfolio](https://kgasil.github.io/portfolio/) · [Estudo de caso / Case study](https://kgasil.github.io/portfolio/cases.html#demands)

<!-- kg-current-training -->
[Formação e experiência atualizadas / Updated education and experience](https://kgasil.github.io/portfolio/resume.html).


Projeto demonstrativo de aplicação **Full Stack** unindo **modelagem relacional em SQL**, **API REST em Python (Flask)** e **interface web (HTML, CSS e JavaScript)** para registro, precificação estimada e acompanhamento de demandas operacionais.
> 🌐 *English version available below:* [Jump to English Version](#english-version)
---

## Arquitetura do Projeto

* **`schema_e_consultas.sql`:** Definição da tabela de demandas, carga inicial de exemplo e consulta agregada por área e status.
* **`app.py`:** API REST com endpoints `GET /api/demandas`, `POST /api/demandas` e `PATCH /api/demandas/<id>/status`, validação de dados e persistência em SQLite.
* **`index.html`:** Interface web para cadastro de novas demandas, visualização tabular e atualização de status em tempo real.

---

## Como executar localmente

Com Python 3 instalado, na pasta do projeto:

```bash
python -m pip install flask
python app.py
```

Acesse http://127.0.0.1:5000. O aplicativo cria `demandas.db` automaticamente; o SQL separado é um exemplo com dados fictícios. Não use dados corporativos reais nem exponha este protótipo sem autenticação e controles de produção.

---

<a id="english-version"></a>

# Demand Control System — Full Stack (SQL, Python & Web)

Demonstrative Full Stack application combining **relational SQL modeling**, a **Python (Flask) REST API**, and a **web interface (HTML, CSS, and JavaScript)** for logging, estimating costs, and tracking operational demands.

## Project Architecture

* `schema_e_consultas.sql`: Defines the demands table, sample initial seed data, and aggregated queries by department and status.
* `app.py`: REST API featuring `GET /api/demandas`, `POST /api/demandas`, and `PATCH /api/demandas/<id>/status` endpoints, input validation, and SQLite persistence.
* `index.html`: Web interface for creating new demands, viewing tabular records, and updating statuses in real time.

## Run locally

From the project folder, with Python 3 installed:

```bash
python -m pip install flask
python app.py
```

Open http://127.0.0.1:5000. The app creates `demandas.db`; the separate SQL file illustrates sample data and reporting. Local demo only: do not expose publicly or store real business data without authentication and production controls.

---

## Testes automatizados / Automated tests

```bash
python -m pip install -r requirements.txt
python -m unittest -v test_app
```

Os testes utilizam um banco temporário para verificar cadastro, atualização de status e entradas inválidas, sem alterar o banco principal. / Tests use a temporary database to check creation, status updates and invalid inputs without modifying the main database.

**Limitação de segurança / Security limitation:** a interface ainda precisa substituir a inserção de dados de usuário via `innerHTML` por operações DOM seguras. Não publique esta demonstração na internet. / The interface still needs safe DOM rendering for user-provided text. Do not expose this demo publicly.
