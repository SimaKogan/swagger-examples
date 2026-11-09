"""Минимальный пример Flask-RESTful: хранение значений по ключу.

Запуск:   python -m examples.flask_restful_simple
Клиент:   python -m examples.flask_restful_client
"""
from flask import Flask, request
from flask_restful import Api, Resource, abort

from examples.common import HOST, debug_enabled, get_port

app = Flask(__name__)
api = Api(app)

todos: dict = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        if todo_id not in todos:
            abort(404, message=f"Todo {todo_id} doesn't exist")
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        if "data" not in request.form:
            abort(400, message="Form field 'data' is required")
        todos[todo_id] = request.form["data"]
        return {todo_id: todos[todo_id]}


api.add_resource(TodoSimple, "/<string:todo_id>")


if __name__ == "__main__":
    app.run(host=HOST, port=get_port(5003), debug=debug_enabled())
