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
    sign = "3310765E77D6230F80858B6BA14BC4FCA7C8CE72F1F6D8FDE891F214A9B9B516"
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
