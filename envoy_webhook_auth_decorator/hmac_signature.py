"""Envoy signature management."""

import hmac
import hashlib


def generator(api_key, timestamp, token):
    message = '{}{}'.format(timestamp, token)
    return hmac.new(bytes(api_key, 'UTF-8'), msg=bytes(message, 'UTF-8'),
                    digestmod=hashlib.sha256).hexdigest().upper()


def is_valid(api_key, timestamp, token, signature):
    return generator(api_key, timestamp, token) == signature
