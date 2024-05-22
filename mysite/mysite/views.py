
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest, **kwargs):
    par = request.GET.get("par")
    print(f'\t{par=}')
    return render(request, "home.html")