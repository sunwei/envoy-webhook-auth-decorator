"""Envoy signature tests."""

from envoy_webhook_auth_decorator import generator
from envoy_webhook_auth_decorator import is_valid

SIGN = "3310765E77D6230F80858B6BA14BC4FCA7C8CE72F1F6D8FDE891F214A9B9B516"
API_KEY = "key"
TIMESTAMP = "23523523"
TOKEN = "token"


def test_signature_generator():
    sign = generator(API_KEY, TIMESTAMP, TOKEN)
    assert sign == SIGN


def test_signature_is_valid():
    assert is_valid(API_KEY, TIMESTAMP, TOKEN, SIGN)
    assert not is_valid(API_KEY, TIMESTAMP, "different token", SIGN)
