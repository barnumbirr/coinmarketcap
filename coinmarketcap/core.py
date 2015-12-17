#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .utils import coin_info
from .utils import update_info
from .utils import top_currencies
from .utils import market_cap_info
from .utils import coinmarketcap_info

def about():
	"""Returns some information about the coinmarketcap module."""

	return '{} v.{} is maintained by {} and available at {}.'.format(__title__, __version__, __author__, __repo__)

def rank(PARAMETER):
	return coin_info(PARAMETER)[0]

def name(PARAMETER):
	return coin_info(PARAMETER)[1]

def short(PARAMETER):
	return coin_info(PARAMETER)[2]

def market_cap(PARAMETER):
	return coin_info(PARAMETER)[3]

def price(PARAMETER):
	return coin_info(PARAMETER)[4]

def coin_supply(PARAMETER):
	return coin_info(PARAMETER)[5]

def market_volume(PARAMETER):
	return coin_info(PARAMETER)[6]

def cap_change_1h(PARAMETER):
	return coin_info(PARAMETER)[7]

def cap_change_24h(PARAMETER):
	return coin_info(PARAMETER)[8]

def cap_change_7d(PARAMETER):
	return coin_info(PARAMETER)[9]

def top(PARAMETER):
	return top_currencies(PARAMETER)

def mineable(PARAMETER):
	try:
		if coin_info(PARAMETER)[10] == '*':
			return 'false'
		if coin_info(PARAMETER)[10] == '**':
			return 'true'
	except IndexError:
		return 'true'

def premined(PARAMETER):
	try:
		if coin_info(PARAMETER)[10] == '**':
			return 'true'
		if coin_info(PARAMETER)[10] == '*':
			return 'false'
	except IndexError:
		return 'false'

def last_updated():
	return update_info()[0]

def total_market_cap():
	return market_cap_info()[1]

def stats():
	return str(coinmarketcap_info()['active_currencies']) + ' Currencies / '\
	+ str(coinmarketcap_info()['active_markets']) + ' Markets / ' \
	+ str(coinmarketcap_info()['active_assets']) + ' Assets'

def coin_summary(PARAMETER):
	keys = ['name', 'rank', 'short', 'market_cap', 'market_volume', 'cap_change_1h',\
	'cap_change_24h', 'cap_change_7d', 'price', 'coin_supply', 'mineable', 'premined']
	values = [name(PARAMETER), rank(PARAMETER), short(PARAMETER), market_cap(PARAMETER),\
	market_volume(PARAMETER), cap_change_1h(PARAMETER), cap_change_24h(PARAMETER),\
	cap_change_7d(PARAMETER), price(PARAMETER), coin_supply(PARAMETER), mineable(PARAMETER),\
	premined(PARAMETER)]
	coin_summary_info = {}
	for i in range(len(keys)):
		coin_summary_info[keys[i]] = values[i]
	return coin_summary_info
