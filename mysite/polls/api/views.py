import logging
from django.http import HttpRequest, JsonResponse

from ..models import Question
from .serializers import QuestionSerializer



logger = logging.getLogger(__name__)
def get_questions(request: HttpRequest):
    qs =Question.objects.all()
    #qs = qs.filter(type="Single")
    objs = qs
    logger.info(f"{objs=}")
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
   
    logger.info(f"{obj.choice_set=}")
    #choices = obj.choice_set.all()
    #logger.info(f"{choices=}")
    serializer = QuestionSerializer(obj)
    logger.info(f"{serializer.data=}")
    #json = serializers.serialize("json", obj)
    return JsonResponse(serializer.data)