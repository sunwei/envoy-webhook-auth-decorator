"""
Envoy webhook authentication decorator.

    :copyright: (c) 2019-2020 by Wayde Sun.
    :license: MIT, see LICENSE for more details.
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from functools import wraps
from . hmac_signature import is_valid


############################################################
# Envoy webhook
############################################################


class AuthenticationError(AssertionError):
    """Thrown when authentication not passed."""

    def __init__(self, value="Envoy webhook callback authentication Failed"):
        self.value = value

    def __str__(self):
        return repr(self.value)


def _raise_exception(exception, exception_message):
    """ This function checks if a exception message is given.

    If there is no exception message, the default behaviour is maintained.
    If there is an exception message, the message is passed to the exception with the 'value' keyword.
    """
    if exception_message is None:
        raise exception()
    else:
        raise exception(exception_message)


def authentication(payload=None, authentication_exception=AuthenticationError, exception_message=None):
    """Add a timeout parameter to a function and return it.

    :param payload: envoy webhook request payload
    :type payload: json
    :param authentication_exception: payload authentication exception
    :type authentication_exception: exception
    :exception_message: exception message
    :type exception_message: str

    decorator the function
    """

    def decorate(func):
        if not payload:
            return func

        @wraps(func)
        def new_function(*args, **kwargs):
            authentication_wrapper = _Authentication(func, payload, authentication_exception, exception_message)
            return authentication_wrapper(*args, **kwargs)

        return new_function

    return decorate


class _Authentication(object):
    """Wrap a function and add a payload (request) attribute to it.

    Instances of this class are automatically generated by the authentication
    function defined above.
    """

    def __init__(self, func, payload, authentication_exception, exception_message):
        """Initialize instance in preparation for being called."""
        self.__payload = payload
        self.__function = func
        self.__authentication_exception = authentication_exception
        self.__exception_message = exception_message
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __call__(self, *args, **kwargs):
        """Execute the embedded function object asynchronously.

        The function given to the constructor is transparently called and
        requires that "ready" be intermittently polled. If and when it is
        True, the "value" property may then be checked for returned data.
        """
        if self._validate():
            return self.__function(*args, **kwargs)

    def _validate(self):
        """Terminate any possible execution of the embedded function."""
        if is_valid(self.__payload['api_key'], self.__payload['timestamp'], self.__payload['token'],
                    self.__payload['signature']):
            return True

        _raise_exception(self.__authentication_exception, self.__exception_message)
