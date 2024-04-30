import datetime

from django.db import models
from django.utils import timezone

QUESTION_TYPES = (
    ("Single", "Single choose"), 
    ("Multiple","Multiple choose")
 )
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    question_note = models.CharField(max_length=200, null=True, blank=True, verbose_name="Note")
    type = models.CharField(max_length=100, choices=QUESTION_TYPES, null=True, default="Single", verbose_name="Question type")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text
    
    def __repr__(self) -> str:
        return f'Question(id={self.id}, question_text={self.question_text}, pub_date={self.pub_date})'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)