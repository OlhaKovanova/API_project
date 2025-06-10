from endpoints.meme import MemeAPI
from utils.assertions import assert_status_ok, assert_status_not_found, assert_meme_equals_by_id


def test_update_existing_meme(meme_api, temp_meme):

    updated_payload = {
        "meme_id": temp_meme,
        "text": "Updated meme text",
        "url": "http://example.com/updated.jpg",
        "tags": ["updated", "funny"],
        "info": {"author": "updated_user"}
    }

    update_response = meme_api.update(**updated_payload)
    assert_status_ok(update_response)

    updated_data = update_response.json()

    expected_data = updated_payload.copy()
    expected_data["id"] = temp_meme
    assert_meme_equals_by_id(expected_data, updated_data)


def test_update_meme_not_found(meme_api):
    non_existent_id = 999_999_999

    # Ensure meme with that ID does not exist
    get_response = meme_api.get_by_id(non_existent_id)
    assert_status_not_found(get_response)

    # Try to update non-existent meme
    response = meme_api.update(
        meme_id=non_existent_id,
        text="Updated text",
        url="http://example.com/updated_meme.jpg",
        tags=["updated", "test"],
        info={"author": "test_user"}
    )
    assert_status_not_found(response)
