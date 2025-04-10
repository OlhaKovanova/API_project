from test_api_meme.endpoints.meme import MemeAPI


def test_get_meme_by_id(token):
    meme_api = MemeAPI(token)

    # 1. Создаём тестовый мем
    create_response = meme_api.create(
        text="Test meme",
        url="http://example.com/test.jpg",
        tags=["test", "get"],
        info={"author": "tester"}
    )
    assert create_response.status_code == 200
    created_meme = create_response.json()
    meme_id = created_meme["id"]

    # 2. Получаем этот мем по ID
    get_response = meme_api.get_by_id(meme_id)
    assert get_response.status_code == 200
    meme_data = get_response.json()

    # 3. Проверяем, что данные совпадают
    assert meme_data["id"] == meme_id
    assert meme_data["text"] == "Test meme"
    assert meme_data["url"] == "http://example.com/test.jpg"
    assert "get" in meme_data["tags"]
    assert meme_data["info"]["author"] == "tester"

    # 4. Удаляем мем после теста
    meme_api.delete(meme_id)


def test_get_all_memes(token):
    meme_api = MemeAPI(token)

    response = meme_api.get_all()

    assert response.status_code == 200

    # Проверяем, что ответ содержит ключ 'data' и его значение является списком
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) >= 0


def test_get_all_meme_with_invalid_token():
    meme_api = MemeAPI("invalid_token")

    response = meme_api.get_all()

    assert response.status_code == 401
