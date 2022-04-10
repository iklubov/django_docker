from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def redirect_view():
    response = redirect('/redirect-success/')
    return response