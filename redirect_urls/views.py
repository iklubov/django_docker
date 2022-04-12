import itertools

from django.http import HttpResponse
from django.shortcuts import redirect

circle_iterator = itertools.cycle(range(5))

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

def cirle_redirect_view(request):
    redirect_index =  next(circle_iterator)
    response = redirect('/redirect_circle_{}/'.format(redirect_index))
    return response
