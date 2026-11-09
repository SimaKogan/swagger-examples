"""Демо safrs: JSON:API + Swagger для моделей SQLAlchemy.

Запуск:   python -m examples.safrs_demo [IP-адрес]
Swagger:  http://127.0.0.1:5005/
"""
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSBase, SafrsApi

from examples.common import debug_enabled, get_port

db = SQLAlchemy()


class User(SAFRSBase, db.Model):
    """
    description: User description
    """

    __tablename__ = "Users"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, default="")
    email = db.Column(db.String, default="")
    books = db.relationship("Book", back_populates="user", lazy="dynamic")


class Book(SAFRSBase, db.Model):
    """
    description: Book description
    """

    __tablename__ = "Books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="")
    user_id = db.Column(db.String, db.ForeignKey("Users.id"))
    user = db.relationship("User", back_populates="books")


def create_api(app, host, port, api_prefix=""):
    api = SafrsApi(app, host=host, port=port, prefix=api_prefix)
    api.expose_object(User)
    api.expose_object(Book)
    print(f"Created API: http://{host}:{port}/{api_prefix}")


def create_app(host="127.0.0.1", port=5005):
    app = Flask("demo_app")
    app.config.update(SQLALCHEMY_DATABASE_URI="sqlite://")
    db.init_app(app)

    with app.app_context():
        db.create_all()
        create_api(app, host, port)
        # Тестовые данные: пользователь и книга, привязанная к нему
        for i in range(200):
            user = User(name=f"user{i}", email=f"email{i}@email.com")
            book = Book(name=f"test book {i}")
            user.books.append(book)

    return app


host = sys.argv[1] if sys.argv[1:] else "127.0.0.1"
port = get_port(5005)
app = create_app(host=host, port=port)

if __name__ == "__main__":
    app.run(host=host, port=port, debug=debug_enabled())
