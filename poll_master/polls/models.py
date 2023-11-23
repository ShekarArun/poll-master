import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    def __str__(self) -> str:
        return f"'{self.question_text}', published {self.pub_date}"

    def was_published_recently(self) -> bool:
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
