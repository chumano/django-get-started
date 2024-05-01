from rest_framework import serializers
from ..models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        #fields = '__all__'
        fields = ["id","question_text"]
        many = True