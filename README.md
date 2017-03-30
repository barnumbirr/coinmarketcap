<h1><img src="https://raw.githubusercontent.com/mrsmn/coinmarketcap-api/master/doc/coinmarketcap.png" height=85 alt="coinmarketcap" title="coinmarketcap">coinmarketcap-api</h1>

[![PyPi Version](http://img.shields.io/pypi/v/coinmarketcap.svg)](https://pypi.python.org/pypi/coinmarketcap/)

**coinmarketcap** is an APACHE licensed library written in Python designed to provide a simple to use API for [coinmarketcap](http://coinmarketcap.com/).

## Installation:

From source use

    $ python setup.py install

or install from PyPi

    $ pip install coinmarketcap

## API Documentation:

This API can currently retrieve the following data from [coinmarketcap](http://coinmarketcap.com/):

- **`GET /v1/ticker/`**
- **`GET /v1/ticker/currency`**

```python
>>> from coinmarketcap import Market
>>> coinmarketcap = Market()
>>> coinmarketcap.ticker(<currency>)
# <currency> can be passed through 'ethereum' or 'ETH' and returns in json

>>> coinmarketcap.ticker('ETH')
>>> coinmarketcap.ticker('ethereum')

# Add VERBOSE=True for a string response, like this:
>>> coinmarketcap.ticker('STEEM', VERBOSE=True)

# Receive all the currencies in a string:
>>> coinmarketcap.ticker(VERBOSE=True)
[
  {
    id: "bitcoin",
    name: "Bitcoin",
    symbol: "BTC",
    rank: 1,
    price_usd: 448.66,
    24h_volume_usd: 84396000,
    market_cap_usd: 6946212888,
    available_supply: 15482200,
    total_supply: 15482200,
    percent_change_1h: 0.47,
    percent_change_24h: -1.61,
    percent_change_7d: 1.25
  },
  {
    id: "ethereum",
    name: "Ethereum",
    symbol: "ETH",
    rank: 2,
    price_usd: 7.28,
    24h_volume_usd: 13419600,
    market_cap_usd: 578917949,
    available_supply: 79512085,
    total_supply: 79512085,
    percent_change_1h: 0.21,
    percent_change_24h: -6.51,
    percent_change_7d: -14.64
  },

  ...
]			
```

- **`GET /v1/global/`**

```python
>>> coinmarketcap.stats(VERBOSE=True)
{
  total_market_cap_usd: 8280726727,
  total_24h_volume_usd: 108644044,
  bitcoin_percentage_of_market_cap: 81.77,
  active_currencies: 690,
  active_assets: 57,
  active_markets: 1902
}		
```


## License:

```
  Apache v2.0 License
  Copyright 2014-2016 Martin Simon

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
HBN : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```
