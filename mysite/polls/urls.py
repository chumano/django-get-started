from django.urls import include, path, re_path

from .views import index

urlpatterns = [
    path("", index, name="index" ),
    path("api/", include("polls.api.urls")), 
]