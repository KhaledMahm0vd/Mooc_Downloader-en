'''
Mooc's request module: includes three commonly used requests: get, post, and head
'''

from time import sleep
from functools import wraps
from socket import timeout, setdefaulttimeout
from urllib import request, parse
from urllib.error import ContentTooShortError, URLError, HTTPError
from Mooc.Mooc_Config import *

__all__ = [
    'RequestFailed', 'request_get', 'request_post', 'request_head', 'request_check'
]

headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")  #Simulate browser here
opener = request.build_opener()  
opener.addheaders = [headers]
request.install_opener(opener)
setdefaulttimeout(TIMEOUT)

class RequestFailed(Exception):
    pass

def request_decorate(count=3):
    def decorate(func):
        @wraps(func)
        def wrap_func(*args, **kwargs):
            cnt = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except (ContentTooShortError, URLError, HTTPError, ConnectionResetError):
                    cnt += 1
                    if cnt >= count:
                        break
                    sleep(0.32)
                except (timeout):
                    break
            raise RequestFailed("request failed")
        return wrap_func
    return decorate

@request_decorate()
def request_get(url, decoding='utf8'):
    '''get'''
    req = request.Request(url=url)
    response = request.urlopen(req, timeout=TIMEOUT)
    text = response.read().decode(decoding)
    response.close()
    return text

@request_decorate()
def request_post(url, data, decoding='utf8'):
    '''post'''
    data = parse.urlencode(data).encode('utf8')
    req = request.Request(url=url, data=data, method='POST')
    response = request.urlopen(req, timeout=TIMEOUT)
    text = response.read().decode(decoding)
    response.close()
    return text

@request_decorate()
def request_head(url):
    '''head'''
    req = request.Request(url=url);
    response = request.urlopen(req, timeout=TIMEOUT)
    header =  dict(response.getheaders())
    response.close()
    return header

@request_decorate(1)
def request_check(url):
    '''Check if the url is accessible'''
    req = request.Request(url=url);
    response = request.urlopen(req, timeout=TIMEOUT//10)
    response.close()
