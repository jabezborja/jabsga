from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Url
from .forms import NewUrlForm, EditUrlForm
import string
import random

def home(request):
    form = NewUrlForm(request.POST or None)

    # Default contexts
    context = {
        "form": form,
        "from": None # Where the user came from? Selection: home, get_url
    }
    
    if request.method == "POST":
        context['from'] = "post" # Set that the user is came from "post"

        if form.is_valid():

            # Generate Random Strings for default URL
            random_url = ''.join(random.choice(string.ascii_letters) for i in range(7))

            # Defaults of the URL
            title = "My Url"
            urlName = random_url
            url = form.cleaned_data['url']
            
            register = Url(
                title=title,
                urlName=urlName,
                url=url
            )

            form = EditUrlForm(None)

            register.save()

            context['form'] = form
            context['title'] = title
            context['urlname'] = urlName
            context['url'] = url

            return render(request, 'home.html', context)

        return render(request, "home.html", context)

    context['from'] = "home" # Set that the user is came from "home"
    return render(request, "home.html", context)

def edit_url(request, url):
    print("Edit URL")

def get_url(request, url):
    context = {
        "from": "get_url", # Set that user is came from getting the url
        "url": None # Default
    }

    # Perform checks
    try:
        url = Url.objects.get(urlName=url) # Try to get the URL that user has entered in the '/<url>' if there's none return 'None' url
        context["url"] = url.url
        return render(request, 'home.html', context)
    except Url.DoesNotExist:
        return render(request, 'home.html', context)
