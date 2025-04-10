import requests

from test_api_meme.utils.token_storage import TokenStorage


class AuthAPI:
    BASE_URL = "http://167.172.172.115:52355"

    @staticmethod
    def get_token():
        token = TokenStorage.get_saved_token()
        if token and TokenStorage.is_token_alive(token):
            return token

        response = requests.post(f"{AuthAPI.BASE_URL}/authorize", json={"name": "test_user"})
        token = response.json().get("token")
        TokenStorage.save_token(token)
        return token
