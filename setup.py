#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'coinmarketcap',
    packages = ['coinmarketcap'],
    version = '5.0.1',
    description = 'Python wrapper around the coinmarketcap.com API.',
    author = 'Martin Simon',
    author_email = 'me@martinsimon.me',
    url = 'https://github.com/barnumbirr/coinmarketcap',
    license = 'Apache v2.0 License',
    install_requires=['requests==2.18.4', 'requests_cache==0.4.13'],
    keywords = ['cryptocurrency', 'API', 'coinmarketcap','BTC', 'Bitcoin', 'LTC', 'Litecoin', 'XRP', 'Ripple', 'ETH', 'Ethereum '],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description = open('README.md','r').read(),
)
