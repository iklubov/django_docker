import requests

# todo cyclic, big body and many choices urls

a = requests.get('http://194.58.118.37:8000/redirect_urls/redirect')
b = requests.get('http://194.58.118.37:8000/redirect-success/')
print(a)

if a.history:
    print(a.url)