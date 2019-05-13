"""Envoy webhook authentication decorator tests."""

import pytest

from envoy_webhook_auth_decorator import authentication, AuthenticationError


def test_auth_decorator_arg():
    @authentication({"api_key": "b", "timestamp": "b", "token": "b", "signature": "b"})
    def f():
        print("testing...")
    with pytest.raises(AuthenticationError):
        f()


def test_no_payload():
    @authentication()
    def f():
        print("testing...")
    f()
