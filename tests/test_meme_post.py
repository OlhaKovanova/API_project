from endpoints.meme import MemeAPI
from utils.assertions import assert_status_ok, assert_status_bad_request, assert_meme_equals_by_id


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
    assert_meme_equals_by_id(expected_data, actual_data)
