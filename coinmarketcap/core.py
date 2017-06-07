#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

class Market(object):

	__SESSION = None
	__DEFAULT_BASE_URL = 'https://api.coinmarketcap.com/v1/'
	__DEFAULT_TIMEOUT = 120

	def __init__(self, base_url = __DEFAULT_BASE_URL, request_timeout = __DEFAULT_TIMEOUT):
		self.base_url = base_url
		self.request_timeout = request_timeout

	@property
	def session(self):
		if not self.__SESSION:
			self._session = requests.Session()
			self._session.headers.update({'Content-Type': 'application/json'})
			self._session.headers.update({'User-agent': 'coinmarketcap - python wrapper \
		around coinmarketcap.com (github.com/mrsmn/coinmarketcap-api)'})
		return self._session

	def __request(self, endpoint, params):
		response_object = self.session.get(self.base_url + endpoint, params = params, timeout = self.request_timeout)

		if response_object.status_code != 200:
			raise Exception('An error occured, please try again.')
		try:
			response = response_object.json()
		except:
			raise Exception("Could not parse response as JSON, response code was %s, bad json content was '%s'" % (response_object.status_code, response_object.content))

		return response

	def ticker(self, currency="", **kwargs):
		"""
        Returns a dict containing one/all the currencies
        Optional parameters:
		(int) limit - only returns the top limit results.
		(string) convert - return price, 24h volume, and market cap in terms of another currency. Valid values are:
		"AUD", "BRL", "CAD", "CHF", "CNY", "EUR", "GBP", "HKD", "IDR", "INR", "JPY", "KRW", "MXN", "RUB"
        """

		params = {}
		params.update(kwargs)
		response = self.__request('ticker/' + currency, params)
		return response

	def stats(self, **kwargs):
		"""
		Returns a dict containing cryptocurrency statistics.
		Optional parameters:
		(string) convert - return 24h volume, and market cap in terms of another currency. Valid values are:
		"AUD", "BRL", "CAD", "CHF", "CNY", "EUR", "GBP", "HKD", "IDR", "INR", "JPY", "KRW", "MXN", "RUB"
		"""

		params = {}
		params.update(kwargs)
		response = self.__request('global/', params)
		return response
