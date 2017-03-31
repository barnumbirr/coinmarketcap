#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

def _reimport(update=False):
    """ Internal function for serves symbols correspondences """
    from os import path
    p = path.dirname(path.abspath(__file__))
    if update == True:
        from sys import path as pth
        pth.insert(1, p)
        import up
        up.update_currencies()
        pth.remove(p)
        if '' in pth:
            pth.remove('')
    with open(p + '/temp/currencies.txt', 'r') as f:
        availables = f.read()
        from ast import literal_eval as l
        return l(availables)

class Market(object):
    def __init__(self, base_url='https://api.coinmarketcap.com/v1/'):
        self.base_url = base_url
        self.opener = urllib2.build_opener()
        self.opener.addheaders.append(('Content-Type', 'application/json'))
        self.opener.addheaders.append(('User-agent', 'coinmarketcap - python wrapper \
        around coinmarketcap.com (github.com/mrsmn/coinmarketcap-api)'))

    def _urljoin(self, *args):
        """ Internal urljoin function because urlparse.urljoin sucks """
        return "/".join(map(lambda x: str(x).rstrip('/'), args))

    def _get(self, api_call, query):
        url = self._urljoin(self.base_url, api_call)
        if query == None:
            response = self.opener.open(url).read()
        else:
            response_url = self._urljoin(url, query)
            response = self.opener.open(response_url).read()
        return response

    def _up(self, param=None):
        """ Internal function for update symbols currencies """
        data = self._get('ticker/', query=param)
        import json, sys
        if int(sys.version[0]) < 3:
            return json.loads(data)
        else:
            return json.loads(data.decode('utf-8'))

    def ticker(self, param=None, VERBOSE=False):
        """ ticker() returns a dict containing all the currencies
            ticker(currency) returns a dict containing only the currency you
            passed as an argument.
            
            VERBOSE=False (as default) -> ticker() return in json
            VERBOSE=True -> ticker() return a string
        """
        if param != None:
            if param.isupper() == True:
                try:
                    availables = _reimport()
                except IOError:
                    availables = _reimport(update=True)
                if param in availables:
                    param = availables.get(param)
                else: # If the coin isn't in the dict
                    availables = _reimport(update=True)
                    if param not in availables:
                        exc = "The currency %s isn't in coinmarketcap" % param
                        raise NameError(exc)
                
        data = self._get('ticker/', query=param)
        if VERBOSE == True:
            return data
        else:
            import json, sys
            if int(sys.version[0]) < 3:
                return json.loads(data)
            else:
                return json.loads(data.decode('utf-8'))
        
        
    def stats(self, VERBOSE=False):
        """ stats() returns a dict containing cryptocurrency statistics.

            VERBOSE=False (as default) -> stats() return a dict
            VERBOSE=True -> stats() return a string
        """
        data = self._get('global/', query=None)
        if VERBOSE == True:
            return data
        else:
            import json, sys
            if int(sys.version[0]) < 3:
                return json.loads(data)
            else:
                return json.loads(data.decode('utf-8'))
