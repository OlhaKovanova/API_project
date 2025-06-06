def assert_status_ok(response):
    assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"


def assert_status_bad_request(response):
    assert response.status_code == 400, f"Expected 400, got {response.status_code}: {response.text}"


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


def assert_is_list(value, field_name="value"):
    assert isinstance(value, list), f"Expected {field_name} to be a list, got {type(value).__name__}"


def assert_meme_equals(expected, actual):
    assert expected["text"] == actual["text"]
    assert expected["url"] == actual["url"]
    assert set(expected["tags"]) == set(actual["tags"])
    assert expected["info"] == actual["info"]
