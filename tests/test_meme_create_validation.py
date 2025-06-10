import pytest

from test_data.meme_invalid_payloads import invalid_meme_payloads
from utils.assertions import assert_status_bad_request


@pytest.mark.parametrize("payload", invalid_meme_payloads)
def test_create_meme_invalid_inputs(meme_api, payload):
    response = meme_api.create(**payload)
    assert_status_bad_request(response)
