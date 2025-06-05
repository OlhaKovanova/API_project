from endpoints.meme import MemeAPI
from utils.assertions import assert_status_ok, assert_status_not_found, assert_status_unauthorized


def test_get_meme_by_id(meme_api, temp_meme):
    # 1. Retrieve meme by ID
    get_response = meme_api.get_by_id(temp_meme)
    assert_status_ok(get_response)
    meme_data = get_response.json()

    # 2. Validate returned fields
    assert meme_data["id"] == temp_meme
    assert meme_data["text"] == "Temp meme"
    assert meme_data["url"] == "http://example.com/delete.jpg"
    assert "temp" in meme_data["tags"]
    assert meme_data["info"]["author"] == "temp"


def test_get_all_memes(meme_api):
    # 1. Get all memes
    response = meme_api.get_all()
    assert_status_ok(response)

    # 2. Response must contain a list in 'data'
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) >= 0


def test_get_all_memes_with_invalid_token():
    # 1. Using an invalid token
    meme_api = MemeAPI("invalid_token")

    response = meme_api.get_all()
    assert_status_unauthorized(response)
