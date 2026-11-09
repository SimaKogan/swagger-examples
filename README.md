# Swagger examples (Flask)

Small collection of Flask apps that show different ways to document a REST API with Swagger / OpenAPI.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Examples

Each example uses its own port, so they can run side by side
(port 5000 is avoided on purpose: on macOS it is taken by AirPlay Receiver).
Override the port with `PORT=...`.

| Command | What it shows | URL |
| --- | --- | --- |
| `python -m examples.flasgger_hello` | flasgger: spec from a YAML file | http://127.0.0.1:5001/apidocs/ |
| `python -m examples.flask_restful_todo` | Flask-RESTful Todo API | http://127.0.0.1:5002/todos |
| `python -m examples.flask_restful_simple` | minimal Flask-RESTful resource | http://127.0.0.1:5003/todo1 |
| `python -m examples.flask_restful_client` | client for the previous example | — |
| `python -m examples.swagger_ui_access` | static `swagger.json` + flask-swagger-ui | http://127.0.0.1:8080/swagger |
| `python -m examples.safrs_demo` | safrs: JSON:API + Swagger for SQLAlchemy models | http://127.0.0.1:5005/ |

Set `FLASK_DEBUG=1` to enable the debugger and auto-reload (local use only).
