#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coinmarketcap import Market
import json

__DATA_FILE = 'symbols.json'
__COLLISION_LOG = 'collisions.log'

if __name__ == "__main__":

    market = Market()
    ticker = market.ticker(limit = 0)

    symbols = {}
    collisions = {}
    for coin in ticker:
        if coin['symbol'] in symbols.keys():
            # A coin with the given symbol already exists.
            collisions[coin['symbol']] = [symbols[coin['symbol']], coin['id']]
            del(symbols[coin['symbol']])
        elif coin['symbol'] in collisions.keys():
            # A collision for the given coin was already detected. This is a
            # further collision.
            collisions[coin['symbol']].append(coin['id'])
        else:
            # This is a new symbol.
            symbols[coin['symbol']] = coin['id']

    # Print all the symbols that had a collision.
    collision_list = []
    for symbol in collisions.keys():
        ids = ", ".join(collisions[symbol])
        print('Symbol collision -  %5s: %s.' % (symbol, ids))
        collision_list.append('%5s: %s\n' % (symbol, ids))

    with open(__DATA_FILE, 'w') as fd:
        json.dump(symbols, fd, indent = 4, sort_keys = True)

    with open(__COLLISION_LOG, 'w') as fd:
        fd.writelines(collision_list)
