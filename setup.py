#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup


setup(
    name = 'coinmarketcap',
    version = '0.6',
    url = 'https://github.com/c0ding/coinmarketcap-api',
    download_url = 'https://github.com/c0ding/coinmarketcap-api/archive/master.zip',
    author = 'c0ding',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['coinmarketcap'],
    description = 'Python API for coinmarketcap.com.',
    long_description = file('README.md','r').read(),
    keywords = ['Scrypt', 'SHA256d', 'cryptocurrency', 'API', 'LTC', 'Litecoin', 'BTC', 'Bitcoin', 'DOGE', 'Dogecoin'],
)
