from endpoints.meme import MemeAPI
from utils.assertions import assert_status_ok, assert_status_not_found, assert_status_unauthorized, \
    assert_response_contains_data_list, \
    assert_meme_equals_by_id, assert_response_contains_data_list


def test_get_meme_by_id(meme_api, temp_meme):
    # 1. Retrieve meme by ID
    get_response = meme_api.get_by_id(temp_meme)
    assert_status_ok(get_response)
    meme_data = get_response.json()

    # 2. Validate returned fields
    expected_data = {
        "id": temp_meme,
        "text": "Temp meme",
        "url": "http://example.com/delete.jpg",
        "tags": ["temp"],
        "info": {"author": "temp"}
    }
    assert_meme_equals_by_id(expected_data, meme_data)


def test_get_all_memes(meme_api):
    response = meme_api.get_all()
    assert_status_ok(response)
    assert_response_contains_data_list(response)


def test_get_all_memes_with_invalid_token():
    # 1. Using an invalid token
    meme_api = MemeAPI("invalid_token")

    response = meme_api.get_all()
    assert_status_unauthorized(response)


def test_try_to_get_nonexistent_meme(meme_api):
    non_existent_id = 999_999_999

    get_response = meme_api.get_by_id(non_existent_id)
    assert_status_not_found(get_response)
