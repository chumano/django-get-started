from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.core import serializers

import logging

from .models import Question
from .serializers import QuestionSerializer

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    objs = Question.objects.all()
    context = {"question": {"name":"chumano"},
               "questions": objs
               }
    return render(request, "question/list.html",  context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, "question/detail.html", {"question": question})

def results(request, question_id):
    pass

def vote(request, question_id):
    pass

def choices(request):
    return render(request, "choice/list.html")