import os
import requests

TOKEN_FILE = "token.txt"


class TokenStorage:
    @staticmethod
    def get_saved_token():
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                return f.read().strip()
        return None

    @staticmethod
    def save_token(token):
        with open(TOKEN_FILE, "w") as f:
            f.write(token)

    @staticmethod
    def is_token_alive(token):
        resp = requests.get(f"http://167.172.172.115:52355/authorize/{token}")
        return resp.status_code == 200
