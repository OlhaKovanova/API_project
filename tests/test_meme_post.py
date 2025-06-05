from endpoints.meme import MemeAPI
from utils.assertions import assert_status_ok, assert_status_bad_request


def test_create_meme(meme_api):
    response = meme_api.create(
        text="Funny meme",
        url="http://example.com/meme.jpg",
        tags=["funny", "test"],
        info={"author": "test_user"}
    )
    assert_status_ok(response)
    data = response.json()
    assert data["text"] == "Funny meme"


def test_create_meme_with_missing_fields(meme_api):
    response = meme_api.create(
        text="Meme with missing fields",
        url="",
        tags=["test"],
        info={"author": "test_user"}
    )
    assert_status_bad_request(response)


def test_create_meme_invalid_url(meme_api):
    response = meme_api.create(
        text="Test meme",
        url="not-a-valid-url",
        tags=[],
        info={}
    )
    assert_status_bad_request(response)

