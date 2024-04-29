
from django.http import HttpRequest, HttpResponse


def welcome(request: HttpRequest, **kwargs):
    print(f'views.welcome({request=}, {kwargs=})')
    par = request.GET.get("par")
    print(f'\t{par=}')
    return HttpResponse("hello from chumano1")