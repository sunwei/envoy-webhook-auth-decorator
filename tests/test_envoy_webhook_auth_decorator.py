"""Envoy webhook authentication decorator tests."""

import pytest

from envoy_webhook_auth_decorator import authentication, AuthenticationError


def test_auth_decorator_wrong_sign():
    @authentication({"api_key": "b", "timestamp": "b", "token": "b", "signature": "b"})
    def f():
        print("testing...")
    with pytest.raises(AuthenticationError):
        f()


def test_auth_decorator_sign():
    sign = "3310765e77d6230f80858b6ba14bc4fca7c8ce72f1f6d8fde891f214a9b9b516"
    api_key = "key"
    timestamp = "23523523"
    token = "token"

    @authentication({"api_key": api_key, "timestamp": timestamp, "token": token, "signature": sign})
    def f():
        return "result"

    res = f()
    assert res == "result"


def test_no_payload():
    @authentication()
    def f():
        print("no payload...")
    f()
