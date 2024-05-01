
from django.urls import path, re_path


from .views import  get_questions, get_question_by_id

urlpatterns = [
    path("questions/<int:object_id>/", get_question_by_id, name="get_question_by_id"),
    path("questions", get_questions, name="questions" ),
]