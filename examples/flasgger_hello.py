"""Hello World + Swagger UI на flasgger.

Запуск:   python -m examples.flasgger_hello
Документация: http://127.0.0.1:5001/apidocs/
"""
import os

from flask import Flask
from flasgger import Swagger, swag_from

from examples.common import HOST, debug_enabled, get_port, install_css_injector

SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "Hello World API",
        "version": "0.1.0",
        "description": "Small example of a Swagger UI document generated with flasgger.",
    },
    "schemes": ["http", "https"],
}

# Оформление Swagger UI: тёмная шапка и изумрудный акцент.
CUSTOM_CSS = """
<style>
  .swagger-ui .topbar { background: #151b24; border-bottom: 1px solid #263041; }
  .swagger-ui .topbar a span { color: #e6edf3; }
  .swagger-ui .info .title { color: #0f9d6e; }
  .swagger-ui .btn.execute { background: #0f9d6e; border-color: #0f9d6e; color: #fff; }
  .swagger-ui .btn.execute:hover { filter: brightness(1.1); }
  .swagger-ui .btn.try-out__btn { border-color: #0f9d6e; color: #0f9d6e; }
  .swagger-ui .opblock.opblock-get { border-color: #0f9d6e; background: rgba(15, 157, 110, .08); }
  .swagger-ui .opblock.opblock-get .opblock-summary-method { background: #0f9d6e; }
  .swagger-ui, .swagger-ui .opblock-summary-description {
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }
</style>
"""

SWAGGER_CONFIG = {
    "headers": [],
    "specs": [
        {
            # Имя endpoint не должно совпадать с именем view-функции.
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "title": "Hello World API",
}

SPEC_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flasgger_hello.yml")

app = Flask(__name__)
swagger = Swagger(app, template=SWAGGER_TEMPLATE, config=SWAGGER_CONFIG)
install_css_injector(app, SWAGGER_CONFIG["specs_route"], CUSTOM_CSS)


@app.route("/")
@swag_from(SPEC_FILE, methods=["GET"])
def hello_world():
    return "Hello World!!!"


if __name__ == "__main__":
    app.run(host=HOST, port=get_port(5001), debug=debug_enabled())
