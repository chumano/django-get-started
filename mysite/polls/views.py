from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core import serializers

import logging

from .models import Question
from .serializers import QuestionSerializer

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_questions(request: HttpRequest):
    objs =Question.objects.all()

    # 1 way
    #json = serializers.serialize("json", objs)
    #return HttpResponse(json,"application/json")

    # 2 way
    serializer = QuestionSerializer(objs, many= True)
    logger.info(f"{serializer.data=}")
    return JsonResponse(serializer.data, safe = False)

def get_question_by_id(request: HttpRequest, object_id : int):
    logger.info(f"{object_id=}")
    obj = Question.objects.get(id=object_id)
    serializer = QuestionSerializer(obj)
    logger.info(f"{serializer.data=}")
    #json = serializers.serialize("json", obj)
    return JsonResponse(serializer.data)