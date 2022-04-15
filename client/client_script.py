from enum import Enum
from urllib.parse import urljoin

import requests
from requests import ConnectionError, TooManyRedirects

ROOT_PATH = 'http://localhost:8000/redirect_urls/'
ARGS_DELIMITER = '_'

class Redirects(Enum):
    CIRCLE = 'redirect_circle/'
    RESPONSE = 'redirect_response{}{}/'
    MULTIPLE = 'redirect_multiple{}{}/'
    BIG_BODY = 'redirect_big_body/'
    CUSTOM_URL = '{}'

class RedirectsCodes(Enum):
    PERMANENT   = 301
    TEMPORARY   = 302


def get_response_path(redirect_type, *args):
    add_url = str(redirect_type.value).format(*args)
    return urljoin(ROOT_PATH, add_url) if redirect_type != Redirects.CUSTOM_URL else add_url


def get_url(redicrectType, *args):
    request = None
    try:
        url = get_response_path(redicrectType, *args)
        request = requests.get(url)
    except ConnectionError as error:
        return error
    except TooManyRedirects as error:
        return error

    print(request)
    if request is not None and request.status_code == 200 and request.history:
        return request.url, request.status_code


print(get_url(Redirects.RESPONSE, ARGS_DELIMITER, RedirectsCodes.PERMANENT.value))
print(get_url(Redirects.RESPONSE, ARGS_DELIMITER, RedirectsCodes.TEMPORARY.value))
print(get_url(Redirects.CIRCLE))
print(get_url(Redirects.MULTIPLE, ARGS_DELIMITER, 10))
print(get_url(Redirects.MULTIPLE, ARGS_DELIMITER, 35))
print(get_url(Redirects.BIG_BODY))
print(get_url(Redirects.CUSTOM_URL, 'http://google.com'))

