#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
import lxml.html


__title__   = 'coinmarketcap'
__version__ = '0.6'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/coinmarketcap-api'
__license__ = 'Apache v2.0 License'


ENTRY_POINT_URL = 'http://coinmarketcap.com/all.html'


def coin_info(PARAMETER):
	raw_data = lxml.html.parse(ENTRY_POINT_URL)
	tree = raw_data.xpath('//tr[@id="id-' + PARAMETER + '"]/td//text()')
	clean_space = map(lambda x: x.strip(), tree)
	coin_details = [x for x in clean_space if x]
	mineable_char = '*'
	premine_char = '**'
	if mineable_char in coin_details:
		coin_details.remove(mineable_char)
		mineable_index = len(coin_details)
		coin_details.insert(mineable_index, mineable_char)
	if premine_char in coin_details:
		coin_details.remove(premine_char)
		premine_index = len(coin_details)
		coin_details.insert(premine_index, premine_char)
	return coin_details


def update_info():
	raw_data = lxml.html.parse(ENTRY_POINT_URL)
	update_details = raw_data.xpath("//p[@class='small']//text()")
	return update_details


def market_cap_info():
	raw_data = lxml.html.parse(ENTRY_POINT_URL)
	market_cap_details = raw_data.xpath("//div[@id='total_market_cap']//text()")
	return market_cap_details


def coinmarketcap_info():
	raw_data = urllib.urlopen('http://coinmarketcap.com/static/generated_pages/global/stats.json')
	coinmarketcap_details = json.load(raw_data)
	return coinmarketcap_details
