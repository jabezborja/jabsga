from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Url
from .forms import NewUrlForm

def home(request):
    form = NewUrlForm(request.POST or None)

    context = {
        "forms": form,
        "from": "home"
    }

    if request.method != "POST":
        return render(request, 'home.html', context)

    if not form.is_valid():
        return render(request, "home.html", context)

    title = form.cleaned_data['title']
    urlName = form.cleaned_data['url_name']
    url = form.cleaned_data['url']

    register = Url(
        title=title,
        urlName=urlName,
        url=url
    )

    register.save()

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
