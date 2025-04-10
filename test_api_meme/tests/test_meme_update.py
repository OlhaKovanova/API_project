from test_api_meme.endpoints.meme import MemeAPI


def test_update_existing_meme(token):
    meme_api = MemeAPI(token)

    # 1. Создаём тестовый мем
    create_response = meme_api.create(
        text="Old text",
        url="http://example.com/old.jpg",
        tags=["test", "old"],
        info={"author": "test_user"}
    )
    assert create_response.status_code == 200
    meme_data = create_response.json()
    meme_id = meme_data["id"]

    # 2. Обновляем мем
    update_response = meme_api.update(
        meme_id=meme_id,
        text="Updated meme text",
        url="http://example.com/updated.jpg",
        tags=["updated", "funny"],
        info={"author": "updated_user"}
    )
    assert update_response.status_code == 200
    updated_data = update_response.json()

    # 3. Проверяем, что данные обновились
    assert updated_data["text"] == "Updated meme text"
    assert updated_data["url"] == "http://example.com/updated.jpg"
    assert "updated" in updated_data["tags"]
    assert updated_data["info"]["author"] == "updated_user"

    # 4. Убираем за собой (удаляем тестовый мем)
    meme_api.delete(meme_id)


def test_update_meme_not_found(token):
    meme_api = MemeAPI(token)

    response = meme_api.update(
        meme_id=99999,  # Не существующий ID
        text="Updated text",
        url="http://example.com/updated_meme.jpg",
        tags=["updated", "test"],
        info={"author": "test_user"}
    )

    assert response.status_code == 404

