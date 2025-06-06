import requests

from endpoints.auth import AuthAPI
from endpoints.meme import MemeAPI
from utils.token_storage import TokenStorage
from utils.assertions import assert_status_forbidden


def test_user_cannot_delete_others_meme():
    auth_api = AuthAPI()
    token_user1 = auth_api.get_token("user1")
    token_user2 = auth_api.get_token("user2")

    meme_api_user1 = MemeAPI(token_user1)
    meme_api_user2 = MemeAPI(token_user2)

    create_response = meme_api_user1.create(
        text="User1's meme",
        url="http://example.com/user1.jpg",
        tags=["owner"],
        info={"author": "user1"}
    )
    meme_id = create_response.json()["id"]

    delete_response = meme_api_user2.delete(meme_id)
    assert_status_forbidden(delete_response)

    # Clean up
    meme_api_user1.delete(meme_id)
