#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml.html import parse

expected_result = ['#', 'Name', 'Symbol', 'Market Cap', 'Price', 'Available Supply', 'Volume (24h)', '% 1h', '% 24h', '% 7d']

def check_table():
	page = parse("http://coinmarketcap.com/all.html")
	result = page.xpath('//tr/th//text()')
	if cmp(expected_result, result) == 0:
		pass
	else:
		raise Exception("Tests failed !")
	
if __name__ == "__main__":
	check_table()
