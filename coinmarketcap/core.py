#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import tempfile
import requests_cache


class Market(object):

    _session = None
    __DEFAULT_BASE_URL = 'https://pro-api.coinmarketcap.com/v1/'
    __DEFAULT_TIMEOUT = 30
    __TEMPDIR_CACHE = True

    def __init__(self, api_key, base_url=__DEFAULT_BASE_URL, request_timeout=__DEFAULT_TIMEOUT, tempdir_cache=__TEMPDIR_CACHE):
        self.api_key = api_key
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
            self._session.headers.update({'X-CMC_PRO_API_KEY': self.api_key})
        return self._session

    def __request(self, endpoint, params):
        response_object = self.session.get(self.base_url + endpoint, params=params, timeout=self.request_timeout)

        try:
            response = json.loads(response_object.text)

            if isinstance(response, list) and response_object.status_code == 200:
                response = [dict(item, **{u'cached': response_object.from_cache}) for item in response]
            if isinstance(response, dict) and response_object.status_code == 200:
                response[u'cached'] = response_object.from_cache

        except Exception as e:
            return e

        return response

    def listings(self, **kwargs):
        """
        This endpoint displays all active cryptocurrency listings in one call. The maximum
        number of results per call is 5000 (there's yet to be 5000 active cryptocurrencies
        in coinmarketcap so it'll display whatever much there are). For every 200
        cryptocurrencies, a credit count will be charged.

        Optional parameters:
        (int) start - return results from rank [start] and above (default is 1)
        (int) limit - return a maximum of [limit] results (default is 100; max is 5000)
        (string) convert - return pricing info in terms of another currency.
                           See available conversions here:
                           https://coinmarketcap.com/api/v1/#section/Standards-and-Conventions
        (string) sort - sorts the list of cryptocurrencies by the following options:
                        "market_cap", "name", "symbol", "date_added", "market_cap", "price",
                        "circulating_supply", "total_supply", "max_supply", "num_market_pairs",
                        "volume_24h", "percent_change_1h", "percent_change_24h", "percent_change_7d"
        (string) sort_dir - direction in which to order cryptocurrencies against the
                            specified sort. Options are "asc" or "desc".
        (string) cryptocurrency_type - type of cryptocurrency to include. By default the type is
                                       "all", but other valid options are "coins" and "tokens".
        """
        params = {}
        params.update(kwargs)
        response = self.__request('cryptocurrency/listings/latest', params=None)
        return response

    def ticker(self, **kwargs):
        """
        This endpoint displays cryptocurrency ticker data in order of rank. 1 credit
        per use.

        REQUIRED parameters:
        (string) id - ID of the cryptocurrency on coinmarketcap (i.e. 1)

        or

        (string) symbol - the symbol of the cryptocurrency (i.e. BTC, ETH)

        Optional parameters:
        (string) convert - return pricing info in terms of another currency.
                           See available conversions here:
                           https://coinmarketcap.com/api/v1/#section/Standards-and-Conventions
        """

        params = {}
        params.update(kwargs)
        response = self.__request('cryptocurrency/quotes/latest' + params)
        return response

    def stats(self, **kwargs):
        """
        This endpoint displays the global data found at the top of coinmarketcap.com.
        1 credit per use.

        Optional parameters:
        (string) convert - return pricing info in terms of another currency.
                           See available conversions here:
                           https://coinmarketcap.com/api/v1/#section/Standards-and-Conventions
        """

        params = {}
        params.update(kwargs)
        response = self.__request('global-metrics/quotes/latest', params)
        return response
