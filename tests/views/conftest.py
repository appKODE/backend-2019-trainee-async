import pytest


@pytest.fixture
async def mock_message_data():
    return {
        "phoneNumber": "89001112233",
        "text": "Hello, world",
        "naming": "nobody",
    }


@pytest.fixture
async def mock_message_bad_data():
    return {
        "phoneNumber": "89001112233",
        "naming": "nobody",
    }
