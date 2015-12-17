#!/usr/bin/env python
# -*- coding: utf-8 -*-

#            _                            _        _
#           (_)                          | |      | |
#   ___ ___  _ _ __  _ __ ___   __ _ _ __| | _____| |_ ___ __ _ _ __
#  / __/ _ \| | '_ \| '_ ` _ \ / _` | '__| |/ / _ \ __/ __/ _` | '_ \
# | (_| (_) | | | | | | | | | | (_| | |  |   <  __/ || (_| (_| | |_) |
#  \___\___/|_|_| |_|_| |_| |_|\__,_|_|  |_|\_\___|\__\___\__,_| .__/
#                                                              | |
#                                                              |_|

__title__   = 'coinmarketcap'
__version__ = '1.0'
__author__ = 'Martin Simon <me@martinsimon.me>'
__repo__    = 'https://github.com/mrsmn/coinmarketcap-api'
__license__ = 'Apache v2.0 License'

from .core import (
	about, rank, name, short, market_cap, price, coin_supply, market_volume,
	cap_change_1h, cap_change_24h, cap_change_7d, top, mineable, premined,
	last_updated, total_market_cap, stats, coin_summary
)
