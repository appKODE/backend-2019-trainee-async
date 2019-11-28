import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


@pytest.fixture
def client(loop, aiohttp_client):
    """
    Базовая фикстура для старта приложения и получения aiohttp-клиента
    """
    from src.main import create_app

    app = loop.run_until_complete(create_app())
    return loop.run_until_complete(aiohttp_client(app))
