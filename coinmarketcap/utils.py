#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib
    from urllib import urlopen
import lxml.html
import time

ENTRY_POINT_URL = 'http://coinmarketcap.com/all/views/all/'
UPDATE_TIMEOUT = 60.0 # in seconds

_raw_data = None
_response_ts = None
def _get_raw_data():
    global _raw_data
    global _response_ts
    if not _raw_data or (_response_ts and time.time() - _response_ts > UPDATE_TIMEOUT):
	_raw_data = lxml.html.parse(ENTRY_POINT_URL)
	_response_ts = time.time()
    return _raw_data


def coin_info(PARAMETER):
	raw_data = _get_raw_data()
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

def top_currencies(PARAMETER):
	raw_data = _get_raw_data()
	row = raw_data.xpath('//tr/td[@class="no-wrap currency-name"]//text()')
	regex = re.compile("(?:[^\n]*(\n+))+")
	currencies_list = list(filter(lambda i: not regex.search(i), row))

	# normalize back to CSS id. Use coin_info(normalize(row[i]))[1] to get equivalent to text() xpath above
	def normalize(currency):
	    css_id = None
	    idx = 0
	    while True:
		try:
		    xpath_components = raw_data.getpath(currency.getparent()).split('/')[:-1 - idx]
		    css_id = raw_data.xpath("/".join(xpath_components))[0].get("id")[3:]
		except:
		    pass
		if css_id:
		    break
		idx +=1
	    return css_id
	currencies_list = [normalize(currency) for currency in currencies_list]

	return currencies_list[:PARAMETER]

def update_info():
	raw_data = _get_raw_data()
	update_details = raw_data.xpath("//p[@class='small']//text()")
	return update_details

def market_cap_info():
	raw_data = _get_raw_data()
	market_cap_details = raw_data.xpath("//div[@id='total_market_cap']//text()")
	return market_cap_details

def coinmarketcap_info():
	raw_data = urlopen('http://coinmarketcap.com/static/generated_pages/global/stats.json').read().decode('utf-8')
	coinmarketcap_details = json.loads(raw_data)
	return coinmarketcap_details
