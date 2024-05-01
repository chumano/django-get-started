from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Q

import logging

from .models import Question, QuestionQuerySet
from .serializers import QuestionSerializer

logger = logging.getLogger(__name__)

# Create your views here.

def index(request: HttpRequest):
    question_type = request.GET.get("type")
    query_date = request.GET.get("date")
    qs = Question.objects.all()
    if question_type is  not None:
        qs = qs.filter(Q(type=question_type))
    if query_date is not None and query_date =="today":
        qs =  Question.objects.published_today()
    
    objs = qs
    num = qs.count()
    context = {"question": {"name":"chumano"},
               "questions": objs,
               "num_questions": num,
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