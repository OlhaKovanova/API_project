import requests

from endpoints.auth import AuthAPI
from endpoints.meme import MemeAPI
from utils.assertions import assert_status_ok, assert_status_unauthorized


def test_get_token_success():
    auth_api = AuthAPI()
    token = auth_api.get_token()
    assert token is not None
    assert isinstance(token, str)


def test_access_protected_without_token():
    meme_api = MemeAPI(token=None)
    response = meme_api.get_all()
    assert_status_unauthorized(response)


def test_token_alive_check():
    auth_api = AuthAPI()
    token = auth_api.get_token()
    response = requests.get(f"{auth_api.BASE_URL}/authorize/{token}")
    assert_status_ok(response)
