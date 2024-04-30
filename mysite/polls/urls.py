from django.urls import path

from .views import index, get_questions, get_question_by_id

urlpatterns = [
    path("", index, name="index" ),
    path("questions/<int:object_id>/", get_question_by_id, name="get_question_by_id"),
    path("questions", get_questions, name="questions" ),
]