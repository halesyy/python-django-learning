import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


"""
1. Cange your models (in models.py).
2. Run python manage.py makemigrations to create migrations for those changes
3. Run python manage.py migrate to apply those changes to the database.
"""

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # def exists(self, pk):
    #     try:
    #         self.objects.get(pk=pk)
    #         return True
    #     except self.DoesNotExist:
    #         return False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

admin.site.register(Question)
admin.site.register(Choice)
