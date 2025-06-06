from endpoints.meme import MemeAPI
from utils.assertions import assert_status_ok, assert_status_not_found


def test_delete_meme(meme_api, temp_meme):
    # Delete temp meme
    delete_response = meme_api.delete(temp_meme)
    assert_status_ok(delete_response)

    # Check that meme was deleted
    get_response = meme_api.get_by_id(temp_meme)
    assert_status_not_found(get_response)


def test_delete_nonexistent_meme(meme_api):
    non_existent_id = 999_999_999

    get_response = meme_api.get_by_id(non_existent_id)
    assert_status_not_found(get_response)

    delete_response = meme_api.delete(non_existent_id)
    assert_status_not_found(delete_response)


def test_delete_already_deleted_meme(meme_api, temp_meme):
    first_delete = meme_api.delete(temp_meme)
    assert_status_ok(first_delete)

    second_delete = meme_api.delete(temp_meme)
    assert_status_not_found(second_delete)
