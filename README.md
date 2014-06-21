# ![icon](https://raw.githubusercontent.com/barnumbirr/coinmarketcap/master/doc/coinmarketcap.png) coinmarketcap

[![PyPi Version](http://img.shields.io/pypi/v/coinmarketcap.svg)](https://pypi.python.org/pypi/coinmarketcap/)

**coinmarketcap** is an APACHE licensed library written in Python providing an easy to use wrapper around the [coinmarketcap.com](http://coinmarketcap.com/) API. This library has been tested with Python 2.7.x and Python 3.6.x and uses.

As of version 5.0.0 this library uses coinmarketcap's ```Public API Version 2``` as ```Public API Version 1``` will be shutdown on **November 30th, 2018**.

## Installation:

From source use

    $ python setup.py install

or install from PyPi

    $ pip install coinmarketcap

## API Documentation:

**Please note that all results are cached for 120 seconds.**

This API can currently retrieve the following data from [coinmarketcap.com](http://coinmarketcap.com/):

#### **`GET /v2/listings/`**
- **`Description`** - This endpoint displays all active cryptocurrency listings in one call. Use the ```id``` field on the ```ticker``` endpoint to query more information on a specific cryptocurrency.
- **`Optional parameters:`**
    - None

```python
>>> from coinmarketcap import Market
>>> coinmarketcap = Market()
>>> coinmarketcap.listings()
{
    "cached": false,
    "data": [
        {
            "symbol": "BTC",
            "website_slug": "bitcoin",
            "id": 1,
            "name": "Bitcoin"
        },
        {
            "symbol": "LTC",
            "website_slug": "litecoin",
            "id": 2,
            "name": "Litecoin"
        },
        {
            "symbol": "NMC",
            "website_slug": "namecoin",
            "id": 3,
            "name": "Namecoin"
        },
        ...
    ],
    "metadata": {
        "timestamp": 1525776852,
        "num_cryptocurrencies": 1597,
        "error": null
    }
}
```

#### **`GET /v2/ticker/`**
- **`Description`** - This endpoint displays cryptocurrency ticker data in order of rank. The maximum number of results per call is ```100```. Pagination is possible by using the ```start``` and ```limit``` parameters.
- **`Optional parameters:`**
    - **(int) start** - return results from rank [start] and above (default is 1)
    - **(int) limit** - return a maximum of [limit] results (default is 100; max is 100)
    - **(string) convert** - return pricing info in terms of another currency.
    Valid fiat currency values are: "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"
    Valid cryptocurrency values are: "BTC", "ETH" "XRP", "LTC", and "BCH"

```python
>>> from coinmarketcap import Market
>>> coinmarketcap = Market()
>>> coinmarketcap.ticker(start=0, limit=3, convert='EUR')
{
    "cached": false,
    "data": {
        "1": {
            "last_updated": 1525778371,
            "name": "Bitcoin",
            "symbol": "BTC",
            "rank": 1,
            "total_supply": 17021800.0,
            "quotes": {
                "USD": {
                    "market_cap": 158065966762.0,
                    "percent_change_7d": 3.19,
                    "price": 9286.09,
                    "percent_change_24h": -0.5,
                    "volume_24h": 7003230000.0,
                    "percent_change_1h": -0.48
                },
                "EUR": {
                    "market_cap": 132684366083.0,
                    "percent_change_7d": 3.19,
                    "price": 7794.96681216,
                    "percent_change_24h": -0.5,
                    "volume_24h": 5878679339.519999,
                    "percent_change_1h": -0.48
                }
            },
            "max_supply": 21000000.0,
            "circulating_supply": 17021800.0,
            "website_slug": "bitcoin",
            "id": 1
        },
        "1027": {
            "last_updated": 1525778355,
            "name": "Ethereum",
            "symbol": "ETH",
            "rank": 2,
            "total_supply": 99305267.0,
            "quotes": {
                "USD": {
                    "market_cap": 73659184992.0,
                    "percent_change_7d": 12.49,
                    "price": 741.745,
                    "percent_change_24h": 2.05,
                    "volume_24h": 3503160000.0,
                    "percent_change_1h": -0.88
                },
                "EUR": {
                    "market_cap": 61831287703.0,
                    "percent_change_7d": 12.49,
                    "price": 622.63855488,
                    "percent_change_24h": 2.05,
                    "volume_24h": 2940636579.839999,
                    "percent_change_1h": -0.88
                }
            },
            "max_supply": null,
            "circulating_supply": 99305267.0,
            "website_slug": "ethereum",
            "id": 1027
        },
        "52": {
            "last_updated": 1525778642,
            "name": "Ripple",
            "symbol": "XRP",
            "rank": 3,
            "total_supply": 99992263539.0,
            "quotes": {
                "USD": {
                    "market_cap": 31994651347.0,
                    "percent_change_7d": -0.95,
                    "price": 0.816643,
                    "percent_change_24h": -0.98,
                    "volume_24h": 469711000.0,
                    "percent_change_1h": -0.96
                },
                "EUR": {
                    "market_cap": 26857078212.0,
                    "percent_change_7d": -0.95,
                    "price": 0.6855097336,
                    "percent_change_24h": -0.98,
                    "volume_24h": 394286686.4639999,
                    "percent_change_1h": -0.96
                }
            },
            "max_supply": 100000000000.0,
            "circulating_supply": 39178259468.0,
            "website_slug": "ripple",
            "id": 52
        }
    },
    "metadata": {
        "timestamp": 1525778464,
        "num_cryptocurrencies": 1597,
        "error": null
    }
}
```

#### **`GET /v2/ticker/{id}`**
- **`Description`** - This endpoint displays ticker data for a specific cryptocurrency. Use the ```id``` field from the ```listings``` endpoint in the URL.
- **`Optional parameters:`**
    - **(string) convert** - return pricing info in terms of another currency.
    Valid fiat currency values are: “AUD”, “BRL”, “CAD”, “CHF”, “CLP”, “CNY”, “CZK”, “DKK”, “EUR”, “GBP”, “HKD”, “HUF”, “IDR”, “ILS”, “INR”, “JPY”, “KRW”, “MXN”, “MYR”, “NOK”, “NZD”, “PHP”, “PKR”, “PLN”, “RUB”, “SEK”, “SGD”, “THB”, “TRY”, “TWD”, “ZAR”
    Valid cryptocurrency values are: “BTC”, “ETH” “XRP”, “LTC”, and “BCH”

```python
>>> coinmarketcap.ticker(1, convert='EUR')
{
    "cached": false,
    "data": {
        "last_updated": 1525778672,
        "name": "Bitcoin",
        "symbol": "BTC",
        "rank": 1,
        "total_supply": 17021800.0,
        "quotes": {
            "USD": {
                "market_cap": 157721275312.0,
                "percent_change_7d": 2.96,
                "price": 9265.84,
                "percent_change_24h": -0.74,
                "volume_24h": 6982350000.0,
                "percent_change_1h": -0.73
            },
            "EUR": {
                "market_cap": 132395023808.0,
                "percent_change_7d": 2.96,
                "price": 7777.96847616,
                "percent_change_24h": -0.74,
                "volume_24h": 5861152166.399999,
                "percent_change_1h": -0.73
            }
        },
        "max_supply": 21000000.0,
        "circulating_supply": 17021800.0,
        "website_slug": "bitcoin",
        "id": 1
    },
    "metadata": {
        "timestamp": 1525778504,
        "error": null
    }
}
```

#### **`GET /v2/global/`**
- **`Description`** - This endpoint displays the global data found at the top of coinmarketcap.com.
- **`Optional parameters:`**
    - **(string) convert** - return pricing info in terms of another currency.
    Valid fiat currency values are: “AUD”, “BRL”, “CAD”, “CHF”, “CLP”, “CNY”, “CZK”, “DKK”, “EUR”, “GBP”, “HKD”, “HUF”, “IDR”, “ILS”, “INR”, “JPY”, “KRW”, “MXN”, “MYR”, “NOK”, “NZD”, “PHP”, “PKR”, “PLN”, “RUB”, “SEK”, “SGD”, “THB”, “TRY”, “TWD”, “ZAR”
    Valid cryptocurrency values are: “BTC”, “ETH” “XRP”, “LTC”, and “BCH”

```python
>>> coinmarketcap.stats(convert='EUR')
{
    "status": {
        "timestamp": 1525778648,
        "error": null
    },
    "cached": false,
    "data": {
        "quotes": {
            "USD": {
                "total_volume_24h": 23318683476.0,
                "total_market_cap": 435375210543.0
            },
            "EUR": {
                "total_volume_24h": 19574262558.0,
                "total_market_cap": 365464400735.0
            }
        },
        "last_updated": 1525778672,
        "bitcoin_percentage_of_market_cap": 36.23,
        "active_cryptocurrencies": 1597,
        "active_markets": 10649
    },
    "metadata": {
        "timestamp": 1525778648,
        "error": null
    }
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
BTC : 1BNFXHPNRtg7LrLUmQWwPUwzoicUi3uP8Q
ETH : 0xd061B7dD794F6EB357bf132172ce06D1B0E5b97B
BCH : qpcmv8vstulfhgdf29fd8sf2g769sszscvaktty2rv
```
