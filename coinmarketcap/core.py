#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import requests
import tempfile
import requests_cache

class Market(object):

	_session = None
	__DEFAULT_BASE_URL = 'https://api.coinmarketcap.com/v2/'
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
			                             coinmarketcap.com (github.com/barnumbirr/coinmarketcap)'})
		return self._session

	def __request(self, endpoint, params):
		response_object = self.session.get(self.base_url + endpoint, params = params, timeout = self.request_timeout)

		try:
			response = json.loads(response_object.text)

			if isinstance(response, list) and response_object.status_code == 200:
				response = [dict(item, **{u'cached':response_object.from_cache}) for item in response]
			if isinstance(response, dict) and response_object.status_code == 200:
				response[u'cached'] = response_object.from_cache

		# rate limiting is detected when the API gives a 200 status code and the response can't be decoded as JSON
		except json.decoder.JSONDecodeError as jsonError:
			return ("Error: This IP address is being rate limited. Wait a few minutes and make sure you aren't exceeding the 30 calls/minute limit")
		except Exception as e:
			return e

		return response

	def listings(self):
		response = self.__request('listings/', params=None)
		return response

	def ticker(self, currency="", **kwargs):

		params = {}
		params.update(kwargs)

		# see https://github.com/barnumbirr/coinmarketcap/pull/28
		if currency:
			currency = str(currency) + '/'

		response = self.__request('ticker/' + currency, params)
		return response

	def stats(self, **kwargs):

		params = {}
		params.update(kwargs)
		response = self.__request('global/', params)
		return response
