"""Setuptools entry point."""
import codecs
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

dirname = os.path.dirname(__file__)

long_description = (
    codecs.open(os.path.join(dirname, 'README.rst'), encoding='utf-8').read() + '\n' +
    codecs.open(os.path.join(dirname, 'CHANGES.rst'), encoding='utf-8').read()
)

setup(
    name='envoy-webhook-auth-decorator',
    version='0.0.2',
    description='Envoy webhook authentication decorator',
    long_description=long_description,
    author='Wayde Sun',
    author_email='wayde.sun@gmail.com',
    url='https://github.com/sunwei/envoy-webhook-auth-decorator',
    packages=['envoy_webhook_auth_decorator'],
    install_requires=[],
    classifiers=CLASSIFIERS)
