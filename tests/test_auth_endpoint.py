import requests

from endpoints.auth import AuthAPI
from endpoints.meme import MemeAPI
from utils.assertions import assert_status_unauthorized, assert_token_valid, assert_token_alive


def test_get_token_success():
    auth_api = AuthAPI()
    token = auth_api.get_token()
    assert_token_valid(token)


def test_access_protected_without_token():
    meme_api = MemeAPI(token=None)
    response = meme_api.get_all()
    assert_status_unauthorized(response)


def test_token_alive_check():
    auth_api = AuthAPI()
    token = auth_api.get_token()
    assert_token_alive(auth_api, token)
