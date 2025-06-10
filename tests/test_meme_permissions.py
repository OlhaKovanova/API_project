import pytest
import requests

from endpoints.auth import AuthAPI
from endpoints.meme import MemeAPI
from utils.token_storage import TokenStorage
from utils.assertions import assert_status_forbidden


@pytest.mark.usefixtures("temp_meme")
def test_user_cannot_delete_others_meme(temp_meme):
    # Get to ken of 2nd user
    token_other_user = AuthAPI().get_token("another_user")
    meme_api_other_user = MemeAPI(token_other_user)

    # Try to delete not your meme
    response = meme_api_other_user.delete(temp_meme)
    assert_status_forbidden(response)
