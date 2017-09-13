#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'coinmarketcap',
    version = '4.1.1',
    url = 'https://github.com/mrsmn/coinmarketcap-api',
    download_url = 'https://github.com/mrsmn/coinmarketcap-api/archive/master.zip',
    author = 'Martin Simon <me@martinsimon.me>',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['coinmarketcap'],
    description = 'Python wrapper around the coinmarketcap.com API.',
    long_description = open('README.md','r').read(),
    install_requires=['requests', 'requests_cache'],
    keywords = ['cryptocurrency', 'API', 'coinmarketcap','BTC', 'Bitcoin', 'LTC', 'Litecoin', 'DOGE', 'Dogecoin', 'ETH', 'Ethereum '],
)
