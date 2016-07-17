#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

class Market(object):

	def __init__(self, base_url='https://api.coinmarketcap.com/v1/'):
		self.base_url = base_url
		self.opener = urllib2.build_opener()
		self.opener.addheaders.append(('Content-Type', 'application/json'))
		self.opener.addheaders.append(('User-agent', 'coinmarketcap - python wrapper \
		around coinmarketcap.com (github.com/mrsmn/coinmarketcap-api)'))

	def _urljoin(self, *args):
		""" Internal urljoin function because urlparse.urljoin sucks """
		return "/".join(map(lambda x: str(x).rstrip('/'), args))

	def _get(self, api_call, query):
		url = self._urljoin(self.base_url, api_call)
		if query == None:
			response = self.opener.open(url).read()
		else:
			response_url = self._urljoin(url, query)
			response = self.opener.open(response_url).read()
		return response

	def ticker(self, param=None):
		""" ticker() returns a dict containing all the currencies
			ticker(currency) returns a dict containing only the currency you
			passed as an argument.
		"""
		data = self._get('ticker/', query=param)
		return data

	def stats(self):
		""" stats() returns a dict containing cryptocurrency statistics. """
		data = self._get('global/', query=None)
		return data
