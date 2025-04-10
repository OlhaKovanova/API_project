from test_api_meme.endpoints.meme import MemeAPI


def test_delete_meme(token):
    meme_api = MemeAPI(token)
    # Создаём временный мем для удаления
    create_response = meme_api.create(
        text="Temp meme",
        url="http://example.com/delete.jpg",
        tags=["temp"],
        info={"author": "temp"}
    )
    meme_id = create_response.json()["id"]

    # Удаляем
    delete_response = meme_api.delete(meme_id)
    assert delete_response.status_code == 200

    # Проверяем, что он действительно удалён
    get_response = meme_api.get_by_id(meme_id)
    assert get_response.status_code == 404


def test_delete_nonexistent_meme(token):
    meme_api = MemeAPI(token)

    # Попытка удалить мем с несуществующим ID
    response = meme_api.delete(meme_id=99999)

    assert response.status_code == 404
