import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    DoesNotExist = None
    objects = None
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)  #


class Choice(models.Model):
    DoesNotExist = None
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# Make sure our custom method worked.
# >>> q = Question.objects.get(pk=1)
# >>> q.was_published_recently()
# True