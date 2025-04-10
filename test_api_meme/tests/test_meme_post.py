from test_api_meme.endpoints.meme import MemeAPI


def test_create_meme(token):
    meme_api = MemeAPI(token)
    response = meme_api.create(
        text="Funny meme",
        url="http://example.com/meme.jpg",
        tags=["funny", "test"],
        info={"author": "test_user"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Funny meme"


def test_create_meme_with_missing_fields(token):
    meme_api = MemeAPI(token)

    # Пропускаем обязательные поля, например, "url"
    response = meme_api.create(
        text="Meme with missing fields",
        url="",
        tags=["test"],
        info={"author": "test_user"}
    )

    assert response.status_code == 400


def test_create_meme_invalid_url(token):
    meme_api = MemeAPI(token)

    response = meme_api.create(
        text="Meme with invalid URL",
        url="http://invalid-url.com/meme.jpg",
        tags=["test", "invalid"],
        info={"author": "test_user"}
    )

    assert response.status_code == 400

