"""Todo API на Flask-RESTful (пример из официальной документации, с исправлениями).

Запуск:   python -m examples.flask_restful_todo
Примеры:  curl http://127.0.0.1:5002/todos
          curl -X POST http://127.0.0.1:5002/todos -d "task=learn Flask"
"""
from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

from examples.common import HOST, debug_enabled, get_port

app = Flask(__name__)
api = Api(app)

TODOS = {
    "todo1": {"task": "build an API"},
    "todo2": {"task": "?????"},
    "todo3": {"task": "check API"},
    "todo4": {"task": "profit!"},
}

parser = reqparse.RequestParser()
parser.add_argument("task", required=True, help="Field 'task' is required")


def next_todo_id(todos: dict) -> str:
    """Следующий свободный идентификатор вида todoN.

    Исходный вариант брал max() по строкам, из-за чего после todo9 ломался
    (строка 'todo9' больше 'todo10') и падал на нестандартных id.
    """
    numbers = [
        int(key[4:]) for key in todos if key.startswith("todo") and key[4:].isdigit()
    ]
    return f"todo{max(numbers, default=0) + 1}"


def abort_if_todo_doesnt_exist(todo_id: str) -> None:
    if todo_id not in TODOS:
        abort(404, message=f"Todo {todo_id} doesn't exist")


class Todo(Resource):
    """Показывает, изменяет и удаляет одну задачу."""

    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return "", 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {"task": args["task"]}
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    """Список всех задач и добавление новой."""

    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = next_todo_id(TODOS)
        TODOS[todo_id] = {"task": args["task"]}
        return TODOS[todo_id], 201


api.add_resource(TodoList, "/todos")
api.add_resource(Todo, "/todos/<todo_id>")


if __name__ == "__main__":
    app.run(host=HOST, port=get_port(5002), debug=debug_enabled())
