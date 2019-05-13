"""Envoy signature tests."""

from envoy_webhook_auth_decorator import generator
from envoy_webhook_auth_decorator import is_valid

SIGN = "3310765e77d6230f80858b6ba14bc4fca7c8ce72f1f6d8fde891f214a9b9b516"
API_KEY = "key"
TIMESTAMP = "23523523"
TOKEN = "token"


def test_signature_generator():
    sign = generator(API_KEY, TIMESTAMP, TOKEN)
    assert sign == SIGN


def test_signature_is_valid():
    assert is_valid(API_KEY, TIMESTAMP, TOKEN, SIGN)
    assert not is_valid(API_KEY, TIMESTAMP, "different token", SIGN)
