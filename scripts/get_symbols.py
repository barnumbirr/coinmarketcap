#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coinmarketcap import Market
import json

__DATA_FILE = 'symbols.json'

if __name__ == "__main__":

    market = Market()
    ticker = market.ticker(limit = 1000)

    symbols = {}
    for coin in ticker:
        symbols[coin['symbol']] = coin['id']

    with open(__DATA_FILE, 'w') as fd:
        json.dump(symbols, fd, indent = 4, sort_keys = True)
