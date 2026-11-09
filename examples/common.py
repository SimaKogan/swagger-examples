"""Общие настройки запуска для всех примеров."""
import os

# Свой порт у каждого примера: на macOS порт 5000 занят AirPlay Receiver,
# а несколько примеров можно запускать одновременно.
HOST = os.environ.get("HOST", "127.0.0.1")


def get_port(default: int) -> int:
    return int(os.environ.get("PORT", default))


def debug_enabled() -> bool:
    return os.environ.get("FLASK_DEBUG", "0") == "1"


def install_css_injector(app, path: str, css: str) -> None:
    """Вставляет <style> в HTML-страницу по адресу `path` (например, Swagger UI).

    Работает независимо от версии библиотеки и её настроек оформления.
    """
    from flask import request

    @app.after_request
    def _inject(response):
        if (
            request.path.rstrip("/") == path.rstrip("/")
            and response.mimetype == "text/html"
            and not response.direct_passthrough
        ):
            html = response.get_data(as_text=True)
            if "</head>" in html:
                response.set_data(html.replace("</head>", css + "</head>", 1))
        return response
