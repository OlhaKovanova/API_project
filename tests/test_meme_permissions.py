import requests
from endpoints.meme import MemeAPI
from utils.token_storage import TokenStorage
from utils.assertions import assert_status_forbidden_or_not_found


def get_token_for_user(username):
    TokenStorage.clear_token(username)
    response = requests.post("http://167.172.172.115:52355/authorize", json={"name": username})
    token = response.json().get("token")
    TokenStorage.save_token(token, username)
    return token


def test_user_cannot_delete_others_meme():
    meme_api_user1 = MemeAPI(get_token_for_user("user1"))
    meme_api_user2 = MemeAPI(get_token_for_user("user2"))

    create_response = meme_api_user1.create(
        text="User1's meme",
        url="http://example.com/user1.jpg",
        tags=["owner"],
        info={"author": "user1"}
    )
    meme_id = create_response.json()["id"]

    delete_response = meme_api_user2.delete(meme_id)
    assert_status_forbidden_or_not_found(delete_response)

    # Clean up
    meme_api_user1.delete(meme_id)
