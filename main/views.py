from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Url
from .forms import NewUrlForm, EditUrlForm
import string
import random

def home(request):
    form = NewUrlForm(request.POST or None)

    context = {
        "forms": form,
        "from": "home"
    }


    # If the method is not POST then just render the html
    if request.method != "POST":
        return render(request, 'home.html', context)

    # Perform form checks
    if not form.is_valid():
        return render(request, "home.html", context)

    random_url = ''.join(random.choice(string.ascii_letters) for i in range(7))

    title = "My Url"
    urlName = random_url
    url = form.cleaned_data['url']
    
    register = Url(
        title=title,
        urlName=urlName,
        url=url
    )

    register.save()

    context['from'] = "post"
    context['title'] = title
    context['urlname'] = urlName
    context['url'] = url

    return render(request, 'home.html', context)

def edit_url(request, url):
    url = Url.objects.get(urlName=url)
    form = EditUrlForm(request.POST or None)

    if request.method != "POST":
        return render(request, 'home.html', context)

    # Perform form checks
    if not form.is_valid():
        return render(request, "home.html", context)

    url.title = form.title
    url.urlName = form.urlName
    url.url = form.url

    url.save()

    return HttpResponseRedirect(f'/')

def get_url(request, url):
    context = {
        "from": "get_url"
    }

    try:
        url = Url.objects.get(urlName=url)
        context["url"] = url.url
        return render(request, 'home.html', context)
    except:
        context["url"] = None
        return render(request, 'home.html', context)
