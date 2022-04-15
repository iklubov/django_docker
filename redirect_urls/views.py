import itertools
from urllib.parse import urljoin

from django.http import HttpResponse
from django.shortcuts import redirect

circle_iterator = itertools.cycle(range(5))

multiple_iterator = None
def multiple_iterator_init(num_requests):
    global multiple_iterator
    multiple_iterator = iter(range(num_requests))

url_base = '/redirect_urls/'

def redirect_response(request, response_match):
    response_status = 301
    if response_match is not None:
        response_status = int(response_match[1:])
    redirect_url = urljoin(url_base, f'redirect_final_{response_status}/')
    response = HttpResponse(status=response_status)
    response['Location'] = redirect_url
    return response

def cirle_redirect_view(request, currentIndex=None):
    try:
        redirect_index = next(circle_iterator)
    except:
        response = redirect(urljoin(url_base, 'redirect_final'))
    else:
        response = redirect(urljoin(url_base, f'redirect_circle_{redirect_index}'))
    return response

def multiple_redirect_view(request, num_requests):
    if multiple_iterator is None:
        multiple_iterator_init(int(num_requests[1:]))
    try:
        redirect_index = next(multiple_iterator)
    except:
        response = redirect(urljoin(url_base, 'redirect_final'))
    else:
        response = redirect(urljoin(url_base, f'redirect_multiple_{redirect_index}'))
    return response

def bigbody_redirect_view(request):
    response = HttpResponse(status=301)
    response['Location'] = urljoin(url_base, 'redirect_final')
    response['content'] = 'abc'*100000
    return response

def redirect_final(request, redirect_code_match):
    redirect_code_match = 'no_code'
    if redirect_code_match is not None:
        redirect_code_match = redirect_code_match[:1]
    return HttpResponse(f"Hello. You're at the final url page with redirect code {redirect_code_match}.")


