<h1><img src="https://raw.githubusercontent.com/c0ding/coinmarketcap-api/master/doc/coinmarketcap.png" height=85 alt="coinmarketcap" title="coinmarketcap">coinmarketcap-api</h1>

[![PyPi Version](http://img.shields.io/pypi/v/coinmarketcap.svg)](https://pypi.python.org/pypi/coinmarketcap/)   [![Downloads](http://img.shields.io/pypi/dm/coinmarketcap.svg)](https://pypi.python.org/pypi/coinmarketcap/)

**coinmarketcap** is an APACHE licensed library written in Python designed to provide a simple to use API for [coinmarketcap](http://coinmarketcap.com/). As coinmarketcap does not provide any API endpoints, this code is pretty dirty. Tested on Python 2.7.11 and 3.4.2.

## Installation:

From source use

    $ python setup.py install

or install from PyPi

    $ pip install coinmarketcap

## API Documentation:

This API can currently retrieve the following data from [coinmarketcap](http://coinmarketcap.com/):

  - Rank:

```python
>>> import coinmarketcap
>>> coinmarketcap.rank('bitcoin')
1
```

  - Name:

```python
>>> coinmarketcap.name('bitcoin')
Bitcoin
```

  - Symbol:

```python
>>> coinmarketcap.short('bitcoin')
BTC
```

  - Market capitalization (last 24h):

```python
>>> coinmarketcap.market_cap('bitcoin')
$ 7,644,402,276
```

  - Price:

```python
>>> coinmarketcap.price('bitcoin')
$ 583.77
```

  - Total coins:

```python
>>> coinmarketcap.coin_supply('bitcoin')
13,094,775
```

  - Market Volume:

```python
>>> coinmarketcap.market_volume('bitcoin')
$ 8,122,070
```

  - Market capitalization change (1 hour):

```python
>>> coinmarketcap.cap_change_1h('bitcoin')
0.17 %
```

  - Market capitalization change (24 hours):

```python
>>> coinmarketcap.cap_change_24h('bitcoin')
-1.07 %
```

  - Market capitalization change (7 days):

```python
>>> coinmarketcap.cap_change_7d('bitcoin')
-2.10 %
```

  - List top 'n' currencies (by market capitalization):

```python
>>> coinmarketcap.top(10)
['bitcoin', 'ethereum', 'ripple', 'litecoin', 'maidsafecoin', 'dogecoin', 'dash', 'peercoin', 'bitshares', 'stellar']
```

  - Mineable:

```python
>>> coinmarketcap.mineable('bitcoin')
true
```

  - Premined:

```python
>>> coinmarketcap.premined('bitcoin')
false
```

  - Coin summary:

```python
>>> coinmarketcap.coin_summary('bitcoin')
{
    "cap_change_1h": "0.17 %",
    "premine": false
    "market_cap": "$ 7,644,402,276",
    "name": "Bitcoin",
    "price": "$ 583.77",
    "rank": "1",
    "short": "BTC",
    "mineable": "true",
    "coin_supply": "13,094,775",
    "market_volume": "$ 8,122,070",
    "cap_change_7d": "-2.10 %",
    "cap_change_24h": "-1.07 %"
}
```

  - Last update:

```python
>>> coinmarketcap.last_updated()
Last updated: Aug 03, 2014  9:05 AM UTC
```

  - Total market capitalization:

```python
>>> coinmarketcap.total_market_cap()
Total Market Cap: $ 8,191,266,103
```

  - Coinmarketcap stats:

```python
>>> coinmarketcap.stats()
501 Currencies / 1532 Markets / 28 Assets
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
