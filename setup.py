#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'coinmarketcap',
    version = '2.0.1',
    url = 'https://github.com/mrsmn/coinmarketcap-api',
    download_url = 'https://github.com/mrsmn/coinmarketcap-api/archive/master.zip',
    author = 'Martin Simon <me@martinsimon.me>',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['coinmarketcap'],
    description = 'Python API for coinmarketcap.com.',
    long_description = open('README.md','r').read(),
    keywords = ['Scrypt', 'SHA256d', 'cryptocurrency', 'API', 'LTC', 'Litecoin', 'BTC', 'Bitcoin', 'DOGE', 'Dogecoin'],
)
