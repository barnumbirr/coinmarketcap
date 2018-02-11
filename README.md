<h1><img src="https://raw.githubusercontent.com/barnumbirr/coinmarketcap/master/doc/coinmarketcap.png" height=85 alt="coinmarketcap" title="coinmarketcap">coinmarketcap</h1>

[![PyPi Version](http://img.shields.io/pypi/v/coinmarketcap.svg)](https://pypi.python.org/pypi/coinmarketcap/)

**coinmarketcap** is an APACHE licensed library written in Python providing an easy to use wrapper around the [coinmarketcap](http://coinmarketcap.com/) API.
This library has been tested with Python 2.7.x and Python 3.6.x.

**Please note that all results are cached for 120 seconds.**

## Installation:

From source use

    $ python setup.py install

or install from PyPi

    $ pip install coinmarketcap

## API Documentation:

This API can currently retrieve the following data from [coinmarketcap](http://coinmarketcap.com/):

- **`GET /v1/ticker/`**
- **`Optional parameters:`**
    - **(int) start** - return results from rank [start] and above
    - **(int) limit** - return a maximum of [limit] results (default is 100, use 0 to return all results)
    - **(string) convert** - return price, 24h volume, and market cap in terms of another currency. Valid values are:
"AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY","KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"

```python
>>> from coinmarketcap import Market
>>> coinmarketcap = Market()
>>> coinmarketcap.ticker(start=0, limit=3, convert='EUR')
[
    {
        "id": "bitcoin",
        "name": "Bitcoin",
        "symbol": "BTC",
        "rank": "1",
        "price_usd": "11710.0",
        "price_btc": "1.0",
        "24h_volume_usd": "19160900000.0",
        "market_cap_usd": "196848905750",
        "available_supply": "16810325.0",
        "total_supply": "16810325.0",
        "max_supply": "21000000.0",
        "percent_change_1h": "-0.57",
        "percent_change_24h": "14.41",
        "percent_change_7d": "-15.59",
        "last_updated": "1516281264",
        "price_eur": "9576.50826",
        "24h_volume_eur": "15669898985.4",
        "market_cap_eur": "160984216216"
    },
    {
        "id": "ethereum",
        "name": "Ethereum",
        "symbol": "ETH",
        "rank": "2",
        "price_usd": "1040.83",
        "price_btc": "0.0895685",
        "24h_volume_usd": "8234010000.0",
        "market_cap_usd": "101020414352",
        "available_supply": "97057554.0",
        "total_supply": "97057554.0",
        "max_supply": null,
        "percent_change_1h": "-1.66",
        "percent_change_24h": "19.22",
        "percent_change_7d": "-15.12",
        "last_updated": "1516281551",
        "price_eur": "851.19701898",
        "24h_volume_eur": "6733822782.06",
        "market_cap_eur": "82615100979.0"
    },
    {
        "id": "ripple",
        "name": "Ripple",
        "symbol": "XRP",
        "rank": "3",
        "price_usd": "1.5284",
        "price_btc": "0.00013153",
        "24h_volume_usd": "9351690000.0",
        "market_cap_usd": "59208905872.0",
        "available_supply": "38739142811.0",
        "total_supply": "99993093880.0",
        "max_supply": "100000000000",
        "percent_change_1h": "-2.32",
        "percent_change_24h": "47.76",
        "percent_change_7d": "-19.55",
        "last_updated": "1516281541",
        "price_eur": "1.2499346904",
        "24h_volume_eur": "7647868192.14",
        "market_cap_eur": "48421398476.0"
    }
]
```

- **`GET /v1/ticker/{id}`**
- **`Optional parameters:`**
    - **(string) convert** - return price, 24h volume, and market cap in terms of another currency. Valid values are:
"AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY","KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"

```python
>>> coinmarketcap.ticker('bitcoin', convert='EUR')
[
    {
        "id": "bitcoin",
        "name": "Bitcoin",
        "symbol": "BTC",
        "rank": "1",
        "price_usd": "11710.0",
        "price_btc": "1.0",
        "24h_volume_usd": "19160900000.0",
        "market_cap_usd": "196848905750",
        "available_supply": "16810325.0",
        "total_supply": "16810325.0",
        "max_supply": "21000000.0",
        "percent_change_1h": "-0.57",
        "percent_change_24h": "14.41",
        "percent_change_7d": "-15.59",
        "last_updated": "1516281264",
        "price_eur": "9576.50826",
        "24h_volume_eur": "15669898985.4",
        "market_cap_eur": "160984216216"
    }
]
```

- **`GET /v1/global/`**
- **`Optional parameters:`**
    - **(string) convert** - return price, 24h volume, and market cap in terms of another currency. Valid values are:
"AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY","KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"


```python
>>> coinmarketcap.stats(convert='EUR')
{
    "total_market_cap_usd": 572724110011.0,
    "total_24h_volume_usd": 62123365544.0,
    "bitcoin_percentage_of_market_cap": 34.29,
    "active_currencies": 895,
    "active_assets": 535,
    "active_markets": 7597,
    "last_updated": 1516281565,
    "total_market_cap_eur": 468377213511.0,
    "total_24h_volume_eur": 50804861082.0
}
```

## License:

```
Copyright 2014-2018 Martin Simon

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
