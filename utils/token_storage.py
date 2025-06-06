import os
import tempfile
import json


class TokenStorage:
    _token_cache = {}

    @staticmethod
    def _get_temp_file(username):
        # Use a secure temp directory
        return os.path.join(tempfile.gettempdir(), f"{username}_token.json")

    @classmethod
    def save_token(cls, token, username="test_user"):
        cls._token_cache[username] = token
        temp_path = cls._get_temp_file(username)
        with open(temp_path, "w") as f:
            json.dump({"token": token}, f)

    @classmethod
    def get_saved_token(cls, username="test_user"):
        if username in cls._token_cache:
            return cls._token_cache[username]
        temp_path = cls._get_temp_file(username)
        if os.path.exists(temp_path):
            with open(temp_path) as f:
                try:
                    return json.load(f).get("token")
                except json.JSONDecodeError:
                    return None
        return None

    @classmethod
    def clear_token(cls, username="test_user"):
        cls._token_cache.pop(username, None)
        temp_path = cls._get_temp_file(username)
        if os.path.exists(temp_path):
            os.remove(temp_path)

    @staticmethod
    def is_token_alive(token):
        import requests
        url = f"http://167.172.172.115:52355/authorize/{token}"
        response = requests.get(url)
        return response.status_code == 200
