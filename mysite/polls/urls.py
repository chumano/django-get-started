from django.http import HttpResponse
from django.urls import include, path, re_path, register_converter

from . import views 

class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value) + 1000 

    def to_url(self, value):
        return "%04d" % value
    
register_converter(FourDigitYearConverter,"yyyy")

def my_view(request, year):
    # This function will be executed when the URL pattern matches
    return HttpResponse(f'{year=} Polls This is the response from the inline view function.')

urlpatterns = [
    path("", views.index, name="index" ),
     # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

    # api
    path("api/", include("polls.api.urls")), 
    path("test/<yyyy:year>/", my_view)
]