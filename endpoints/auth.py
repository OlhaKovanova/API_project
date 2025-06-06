import requests
from utils.token_storage import TokenStorage


class AuthAPI:
    BASE_URL = "http://167.172.172.115:52355"

    @staticmethod
    def get_token(username=None):
        username = username or "test_user"

        token = TokenStorage.get_saved_token(username)
        if token and TokenStorage.is_token_alive(token):
            return token

        response = requests.post(f"{AuthAPI.BASE_URL}/authorize", json={"name": username})
        assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"

        token = response.json().get("token")
        TokenStorage.save_token(token, username)
        return token

    @staticmethod
    def is_token_alive(token):
        response = requests.get(f"{AuthAPI.BASE_URL}/authorize/{token}")
        return response.status_code == 200
