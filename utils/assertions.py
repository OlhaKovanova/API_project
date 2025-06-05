def assert_status_ok(response):
    assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"


def assert_status_bad_request(response):
    assert response.status_code == 400, f"Expected 400, got {response.status_code}: {response.text}"


def assert_status_not_found(response):
    assert response.status_code == 404, f"Expected 404, got {response.status_code}: {response.text}"


def assert_status_unauthorized(response):
    assert response.status_code == 401, f"Expected 401, got {response.status_code}: {response.text}"


def assert_status_forbidden_or_not_found(response):
    assert response.status_code in [403, 404], f"Expected 403 or 404, got {response.status_code}: {response.text}"
