<h1><img src="https://raw.githubusercontent.com/c0ding/coinmarketcap-api/master/doc/coinmarketcap.png" height=85 alt="coinmarketcap" title="coinmarketcap">coinmarketcap-api</h1>

[![PyPi Version](http://img.shields.io/pypi/v/coinmarketcap.svg)](https://pypi.python.org/pypi/coinmarketcap/)   [![Downloads](http://img.shields.io/pypi/dm/coinmarketcap.svg)](https://pypi.python.org/pypi/coinmarketcap/)


**coinmarketcap** is an APACHE licensed library written in Python designed to provide a simple to use API for [coinmarketcap](http://coinmarketcap.com/). As coinmarketcap does not provide any API endpoints, this code is pretty dirty.

## Installation:

From source use

    $ python setup.py install

or install from PyPi

    $ pip install coinmarketcap

## API Documentation:

This API can currently retrieve the following data from [coinmarketcap](http://coinmarketcap.com/):

  - Rank:

```
>>> import coinmarketcap
>>> coinmarketcap.rank('btc')
1
```

  - Name:

```
>>> coinmarketcap.name('btc')
Bitcoin
```

  - Market capitalization (last 24h):

```
>>> coinmarketcap.market_cap('btc')
$ 7,768,506,597
```

  - Price:

```
>>> coinmarketcap.price('btc')
$ 600.77
```

  - Total coins:

```
>>> coinmarketcap.total_coins('btc')
12,930,825 BTC
```

  - Market Volume:

```
>>> coinmarketcap.market_volume('btc')
$ 10,744,269
```

  - Market capitalization change (last 24h):

```
>>> coinmarketcap.market_cap_change('btc')
+0.79 %
```

  - Coin summary:

```
>>> coinmarketcap.coin_summary('btc')
{
    "market_cap": "$ 8,401,445,207",
    "name": "Bitcoin",
    "price": "$ 647.75",
    "rank": "1",
    "coin_supply": "12,970,100 BTC",
    "market_cap_change": "+1.39 %",
    "market_volume": "$ 37,689,775"
}
```

  - Last update:

```
>>> coinmarketcap.last_updated()
Last updated: Jun 22, 2014  3:45 PM UTC
```

  - Total market capitalization:

```
>>> coinmarketcap.total_market_cap()
Total Market Cap: $ 8,408,262,217
```

  - Total currencies available:

```
>>> coinmarketcap.total_currencies()
344 Currencies
```

## License:

```
  Apache v2.0 License
  Copyright 2014 Martin Simon

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
