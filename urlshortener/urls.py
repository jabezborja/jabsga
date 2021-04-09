from django.contrib import admin
from django.urls import path
from main.views import home, get_url, edit_url
from api.views import api_home, api_get

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

    path('<url>', get_url),
    path('<url>/edit', edit_url),

    # API
    path('api/', api_home),
    path('api/get/<url>', api_get)
]
