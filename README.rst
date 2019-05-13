Envoy webhook authentication decorator
======================================

|Build Status| |Pypi Status| |Coveralls Status|

Installation
------------

From source code:

::

    python setup.py install

From pypi:

::

    pip install envoy-webhook-auth-decorator

Usage
-----

::

    import envoy_webhook_auth_decorator

    @envoy_webhook_auth_decorator.@authentication({"api_key": ..., "timestamp": ..., "token": ..., "signature": ...})
    def mytest():
        print("Testing...")

    if __name__ == '__main__':
        mytest()


License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

See `License file <https://github.com/sunwei/envoy-webhook-auth-decorator/blob/master/LICENSE>`_

.. |Build Status| image:: https://travis-ci.com/sunwei/envoy-webhook-auth-decorator.svg?branch=master
   :target: https://travis-ci.com/sunwei/envoy-webhook-auth-decorator
.. |Pypi Status| image:: https://badge.fury.io/py/envoy-webhook-auth-decorator.svg
   :target: https://badge.fury.io/py/envoy-webhook-auth-decorator
.. |Coveralls Status| image:: https://coveralls.io/repos/github/sunwei/envoy-webhook-auth-decorator/badge.svg?branch=master
   :target: https://coveralls.io/github/sunwei/envoy-webhook-auth-decorator?branch=master

