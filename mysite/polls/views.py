from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core import serializers

import logging

from .models import Question
from .serializers import QuestionSerializer

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    return render(request, "question/list.html")

