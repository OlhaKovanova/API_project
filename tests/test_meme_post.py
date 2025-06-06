from endpoints.meme import MemeAPI
from utils.assertions import assert_status_ok, assert_status_bad_request, assert_meme_equals


def test_create_meme(meme_api):
    expected_data = {
        "text": "Funny meme",
        "url": "http://example.com/meme.jpg",
        "tags": ["funny", "test"],
        "info": {"author": "test_user"}
    }
    response = meme_api.create(**expected_data)
    assert_status_ok(response)
    actual_data = response.json()
    assert_meme_equals(expected_data, actual_data)


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

