#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import requests_cache

class Market(object):

	_session = None
	__DEFAULT_BASE_URL = 'https://api.coinmarketcap.com/v1/'
	__DEFAULT_TIMEOUT = 120

	def __init__(self, base_url = __DEFAULT_BASE_URL, request_timeout = __DEFAULT_TIMEOUT):
		self.base_url = base_url
		self.request_timeout = request_timeout

	@property
	def session(self):
		if not self._session:
			self._session = requests_cache.core.CachedSession(cache_name='coinmarketcap_cache', backend='sqlite', expire_after=120)
			self._session.headers.update({'Content-Type': 'application/json'})
			self._session.headers.update({'User-agent': 'coinmarketcap - python wrapper \
		around coinmarketcap.com (github.com/mrsmn/coinmarketcap-api)'})
		return self._session

	def __request(self, endpoint, params):
		response_object = self.session.get(self.base_url + endpoint, params = params, timeout = self.request_timeout)

		if response_object.status_code != 200:
			raise Exception('An error occured, please try again.')
		try:
			response = json.loads(response_object.text)
			if isinstance(response, list):
				response = [dict(item, **{u'cached':response_object.from_cache}) for item in response]
			if isinstance(response, dict):
				response[u'cached'] = response_object.from_cache
		except requests.exceptions.RequestException as e:
			return e

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
