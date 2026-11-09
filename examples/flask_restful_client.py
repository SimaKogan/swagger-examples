"""Клиент для examples.flask_restful_simple (раньше это был req_todo.py).

Сначала запустите сервер:  python -m examples.flask_restful_simple
Затем:                     python -m examples.flask_restful_client
"""
import os
import sys

import requests

BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:5003")


def show(response: requests.Response) -> None:
    response.raise_for_status()
    print(response.status_code, response.json())


def main() -> int:
    try:
        show(requests.put(f"{BASE_URL}/todo1", data={"data": "Remember the milk"}, timeout=5))
        show(requests.get(f"{BASE_URL}/todo1", timeout=5))
        show(requests.put(f"{BASE_URL}/todo2", data={"data": "Change my brakepads"}, timeout=5))
        show(requests.get(f"{BASE_URL}/todo2", timeout=5))
    except requests.ConnectionError:
        print(f"Cannot connect to {BASE_URL}. Is the server running?", file=sys.stderr)
        return 1
    except requests.HTTPError as error:
        print(f"Request failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
