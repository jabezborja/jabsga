from django.shortcuts import render
from main.models import Url

def api_home(request):
    context = {
        "request": "welcome" 
    }
    return render(request, 'api/api_home.html', context)

def api_get(request, url):
    try:
        url = Url.objects.get(urlName=url)
    except:
        url = "null"

    context = {
        "request": "get",
        "content": url
    }
    return render(request, 'api/api_home.html', context)

def api_post(request, url):
    return render(request, 'api/api_home.html', context)