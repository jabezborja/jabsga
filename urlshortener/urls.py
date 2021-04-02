from django.contrib import admin
from django.urls import path
from main.views import home, get_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

    path('<url>', get_url)
]
