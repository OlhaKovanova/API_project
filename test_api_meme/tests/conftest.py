import pytest

from test_api_meme.endpoints.auth import AuthAPI


@pytest.fixture(scope="session")
def token():
    return AuthAPI.get_token()
