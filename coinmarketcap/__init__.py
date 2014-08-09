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
__version__ = '0.6'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/coinmarketcap-api'
__license__ = 'Apache v2.0 License'


import coinmarketcap_utils


from coinmarketcap_api import (
	about, rank, name, short, market_cap, price, coin_supply, market_volume,
	cap_change_1h, cap_change_24h, cap_change_7d, mineable, premined, 
	last_updated, total_market_cap, stats, coin_summary
)
