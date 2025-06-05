from endpoints.meme import MemeAPI
from utils.assertions import assert_status_ok, assert_status_not_found, assert_status_unauthorized


def test_update_existing_meme(meme_api, temp_meme):
    # 1. Update meme with new data
    update_response = meme_api.update(
        meme_id=temp_meme,
        text="Updated meme text",
        url="http://example.com/updated.jpg",
        tags=["updated", "funny"],
        info={"author": "updated_user"}
    )
    assert_status_ok(update_response)
    updated_data = update_response.json()

    # 2. Verify updates
    assert updated_data["text"] == "Updated meme text"
    assert updated_data["url"] == "http://example.com/updated.jpg"
    assert "updated" in updated_data["tags"]
    assert updated_data["info"]["author"] == "updated_user"


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