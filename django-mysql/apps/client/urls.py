from django.urls import path

from apps.client.views import home


urlpatterns = [
    path("", home, name="home"),
]
