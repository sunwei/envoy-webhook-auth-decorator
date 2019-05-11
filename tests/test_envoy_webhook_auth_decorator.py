"""Envoy webhook authentication decorator tests."""

import pytest

from envoy_webhook_auth_decorator import authentication, AuthenticationError


@pytest.fixture(params={"a": "b"})
def get_payload(request):
    """Use signals for timing out or not."""
    return request.param


def test_auth_decorator_arg():
    @authentication(get_payload)
    def f():
        print("testing...")
    with pytest.raises(AuthenticationError):
        f()
