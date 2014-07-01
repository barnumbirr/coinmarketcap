#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lxml.html

__title__   = 'coinmarketcap'
__version__ = '0.3'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/coinmarketcap-api'
__license__ = 'Apache v2.0 License'

ENTRY_POINT_URL = 'http://coinmarketcap.com/all.html'

def coin_info(PARAMETER):
	raw_data = lxml.html.parse(ENTRY_POINT_URL)
	tree = raw_data.xpath('//tr[@id="id-' + PARAMETER + '"]/td//text()')
	coin_details = [x for x in tree if x != ' ']
	return coin_details


def update_info():
	raw_data = lxml.html.parse(ENTRY_POINT_URL)
	update_details = raw_data.xpath("//p[@class='small']//text()")
	return update_details


def market_cap_info():
	raw_data = lxml.html.parse(ENTRY_POINT_URL)
	market_cap_details = raw_data.xpath("//div[@id='total_market_cap']//text()")
	return market_cap_details


def total_currencies_info():
	raw_data = lxml.html.parse(ENTRY_POINT_URL)
	total_currencies_details = raw_data.xpath("//div[@class='pull-right small']//text()")
	return total_currencies_details[0]
