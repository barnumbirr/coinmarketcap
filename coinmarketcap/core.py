#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import requests
import tempfile
import requests_cache

class Market(object):

	_session = None
	__DEFAULT_BASE_URL = 'https://api.coinmarketcap.com/v1/'
	__DEFAULT_TIMEOUT = 30
	__TEMPDIR_CACHE = True

	def __init__(self, base_url = __DEFAULT_BASE_URL, request_timeout = __DEFAULT_TIMEOUT, tempdir_cache = __TEMPDIR_CACHE):
		self.base_url = base_url
		self.request_timeout = request_timeout
		self.cache_filename = 'coinmarketcap_cache'
		self.cache_name = os.path.join(tempfile.gettempdir(), self.cache_filename) if tempdir_cache else self.cache_filename

	@property
	def session(self):
		if not self._session:
			self._session = requests_cache.core.CachedSession(cache_name=self.cache_name, backend='sqlite', expire_after=120)
			self._session.headers.update({'Content-Type': 'application/json'})
			self._session.headers.update({'User-agent': 'coinmarketcap - python wrapper around \
														 coinmarketcap.com (github.com/mrsmn/coinmarketcap-api)'})
		return self._session

	def __request(self, endpoint, params):
		response_object = self.session.get(self.base_url + endpoint, params = params, timeout = self.request_timeout)

		try:
			response = json.loads(response_object.text)

			if isinstance(response, list) and response_object.status_code == 200:
				response = [dict(item, **{u'cached':response_object.from_cache}) for item in response]
			if isinstance(response, dict) and response_object.status_code == 200:
				response[u'cached'] = response_object.from_cache

		except Exception as e:
			return e

		return response

	def ticker(self, currency="", **kwargs):
		"""
        Returns a list of dicts containing one/all the currencies

        Optional parameters:

        GET /ticker/

		(int) start - return results from rank [start] and above
		(int) limit - return a maximum of [limit] results (default is 100, use 0 to return all results)
		(string) convert - return price, 24h volume, and market cap in terms of another currency. Valid values are:
				 "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS",
				 "INR", "JPY","KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB",
				 "TRY", "TWD", "ZAR"


		GET /ticker/{id}

		(string) convert - return price, 24h volume, and market cap in terms of another currency. Valid values are:
				 "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS",
				 "INR", "JPY","KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB",
				 "TRY", "TWD", "ZAR"
		Misc:

		All 'last_updated' fields are unix timestamps.
        """

		params = {}
		params.update(kwargs)

		# see https://github.com/mrsmn/coinmarketcap/pull/28
		if currency:
			currency = currency + '/'

		response = self.__request('ticker/' + currency, params)
		return response

	def stats(self, **kwargs):
		"""
		Returns a dict containing cryptocurrency statistics.

		Optional parameters:

		(string) convert - return 24h volume, and market cap in terms of another currency. Valid values are:
				 "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS",
				 "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB",
				 "TRY", "TWD", "ZAR"

		Misc:

		All 'last_updated' fields are unix timestamps.
		"""

		params = {}
		params.update(kwargs)
		response = self.__request('global/', params)
		return response
