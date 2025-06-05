from utils.assertions import assert_status_bad_request


def test_create_meme_with_invalid_url(meme_api):
    response = meme_api.create(
        text="Invalid URL meme",
        url="not-a-valid-url",
        tags=["test"],
        info={"author": "bad"}
    )
    assert_status_bad_request(response)


def test_create_meme_with_missing_text(meme_api):
    response = meme_api.create(
        text="",
        url="http://example.com/image.jpg",
        tags=["test"],
        info={"author": "bad"}
    )
    assert_status_bad_request(response)


def test_create_meme_with_non_list_tags(meme_api):
    response = meme_api.create(
        text="Tags not list",
        url="http://example.com/image.jpg",
        tags="notalist",
        info={"author": "bad"}
    )
    assert_status_bad_request(response)


def test_create_meme_with_invalid_info(meme_api):
    response = meme_api.create(
        text="Invalid info",
        url="http://example.com/image.jpg",
        tags=["test"],
        info={"author": 123}  # assuming only strings are valid
    )
    assert_status_bad_request(response)
