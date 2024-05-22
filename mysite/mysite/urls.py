"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path, register_converter
from django.contrib.auth.views import LoginView, LogoutView

# from .views import welcome as wel
from . import views
class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value
    
register_converter(FourDigitYearConverter,"yyyy")

def my_view(request, year):
    # This function will be executed when the URL pattern matches
    return HttpResponse(f'{year=} This is the response from the inline view function.')

urlpatterns = [
    path('', views.home ,name="home"),
    path('login/', LoginView.as_view(template_name ="auth/login.html"), name="login"),
    path('logout/', LogoutView.as_view() ,name="logout"),
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls")),
    path("test/<yyyy:year>/", my_view)
]

