#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coinmarketcap_utils import coin_info
from coinmarketcap_utils import update_info
from coinmarketcap_utils import market_cap_info
from coinmarketcap_utils import total_currencies_info

__title__   = 'coinmarketcap'
__version__ = '0.2'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/coinmarketcap-api'
__license__ = 'Apache v2.0 License'


def about():
	"""Returns some information about the coinmarketcap module."""

	return '{} v.{} is maintained by {} and available at {}.'.format(__title__, __version__, __author__, __repo__)

	
def rank(PARAMETER):
	return coin_info(PARAMETER)[0]

	
def name(PARAMETER):
	return coin_info(PARAMETER)[1]

	
def market_cap(PARAMETER):
	return coin_info(PARAMETER)[2]

	
def price(PARAMETER):
	return coin_info(PARAMETER)[3]


def total_coins(PARAMETER):
	return coin_info(PARAMETER)[4]


def market_volume(PARAMETER):
	return coin_info(PARAMETER)[5]


def market_cap_change(PARAMETER):
	return coin_info(PARAMETER)[6]

	
def last_updated():
	return update_info()[0]

	
def total_market_cap():
	return market_cap_info()[1] + market_cap_info()[2]


def total_currencies():
	return total_currencies_info()
