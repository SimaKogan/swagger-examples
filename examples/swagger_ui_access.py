"""Access API с готовым swagger.json и flask-swagger-ui.

Запуск:   python -m examples.swagger_ui_access
Swagger:  http://127.0.0.1:8080/swagger
"""
from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

from examples.common import HOST, debug_enabled, get_port

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

app = Flask(__name__)

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Access API",
        "docExpansion": "list",
        "displayRequestDuration": True,
        "tryItOutEnabled": True,
        "defaultModelsExpandDepth": 0,
    },
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


@app.route("/")
def home():
    return jsonify({"message": "app up and running successfully"})


@app.route("/access", methods=["POST"])
def access():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    name = data.get("name", "dipto")
    server = data.get("server", "server1")
    if not isinstance(name, str) or not isinstance(server, str):
        return jsonify({"error": "'name' and 'server' must be strings"}), 400

    return jsonify({"message": f"User {name} received access to server {server}"})


if __name__ == "__main__":
    app.run(host=HOST, port=get_port(8080), debug=debug_enabled())
