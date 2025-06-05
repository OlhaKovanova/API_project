import os
import requests

TOKEN_FILE = "token.txt"


class TokenStorage:
    _tokens = {}

    @staticmethod
    def get_saved_token(username="test_user"):
        return TokenStorage._tokens.get(username)

    @staticmethod
    def save_token(token, username="test_user"):
        TokenStorage._tokens[username] = token

    @staticmethod
    def is_token_alive(token):
        import requests
        url = f"http://167.172.172.115:52355/authorize/{token}"
        response = requests.get(url)
        return response.status_code == 200

    @staticmethod
    def clear_token(username=None):
        if username:
            TokenStorage._tokens.pop(username, None)
        else:
            TokenStorage._tokens = {}

