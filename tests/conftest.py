import pytest
from endpoints.auth import AuthAPI
from endpoints.meme import MemeAPI


@pytest.fixture(scope="session")
def token(self=None):
    return AuthAPI.get_token(self)


@pytest.fixture
def meme_api(token):
    return MemeAPI(token)


@pytest.fixture
def temp_meme(meme_api):
    response = meme_api.create(
        text="Temp meme",
        url="http://example.com/delete.jpg",
        tags=["temp"],
        info={"author": "temp"}
    )
    meme_id = response.json()["id"]
    yield meme_id
    # cleanup
    meme_api.delete(meme_id)
