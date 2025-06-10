def assert_status_ok(response):
    assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"


def assert_status_bad_request(response):
    assert response.status_code == 400, f"Expected 400, got {response.status_code}: {response.text}"


def assert_meme_creation_bad_request(meme_api, text, url, tags, info):
    response = meme_api.create(text, url, tags, info)
    assert_status_bad_request(response)


def assert_status_not_found(response):
    assert response.status_code == 404, f"Expected 404, got {response.status_code}: {response.text}"


def assert_status_unauthorized(response):
    assert response.status_code == 401, f"Expected 401, got {response.status_code}: {response.text}"


def assert_status_forbidden(response):
    assert response.status_code == 403, f"Expected 403, got {response.status_code}: {response.text}"


def assert_token_valid(token):
    assert token is not None, "Expected non-null token"
    assert isinstance(token, str), f"Expected token to be string, got {type(token)}"
    assert len(token) > 0, "Expected token to be non-empty string"


def assert_token_alive(auth_api, token):
    assert auth_api.is_token_alive(token), "Expected token to be alive but it was not"


def assert_response_contains_data_list(response):
    data = response.json()
    assert "data" in data, "Response JSON does not contain 'data' field"
    assert isinstance(data["data"], list), f"Expected 'data' to be a list, got {type(data['data']).__name__}"


def assert_meme_equals_by_id(expected, actual):
    # Compare IDs only if the expected dictionary contains an 'id' key
    if "id" in expected:
        assert str(expected["id"]) == str(actual["id"]), f"Expected id {expected.get('id')}, got {actual['id']}"
    assert expected["text"] == actual["text"], f"Expected text {expected['text']}, got {actual['text']}"
    assert expected["url"] == actual["url"], f"Expected url {expected['url']}, got {actual['url']}"
    assert expected["tags"] == actual["tags"], f"Expected tags {expected['tags']}, got {actual['tags']}"
    assert expected["info"] == actual["info"], f"Expected info {expected['info']}, got {actual['info']}"
