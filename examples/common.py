"""Общие настройки запуска для всех примеров."""
import os

# Свой порт у каждого примера: на macOS порт 5000 занят AirPlay Receiver,
# а несколько примеров можно запускать одновременно.
HOST = os.environ.get("HOST", "127.0.0.1")


def get_port(default: int) -> int:
    return int(os.environ.get("PORT", default))


def debug_enabled() -> bool:
    return os.environ.get("FLASK_DEBUG", "0") == "1"
