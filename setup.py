#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'coinmarketcap',
    version = '3.0',
    url = 'https://github.com/mrsmn/coinmarketcap-api',
    download_url = 'https://github.com/mrsmn/coinmarketcap-api/archive/master.zip',
    author = 'Martin Simon <me@martinsimon.me>',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['coinmarketcap'],
    description = 'Python wrapper for the coinmarketcap.com API.',
    long_description = open('README.md','r').read(),
    install_requires=['requests'],
    keywords = ['cryptocurrency', 'API', 'BTC', 'Bitcoin', 'LTC', 'Litecoin', 'DOGE', 'Dogecoin', 'ETH', 'Ethereum '],
)
