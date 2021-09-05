from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField()
    ticker = models.CharField(max_length=25)
    investmentAmount = models.IntegerField(default=100)
    tickerarray = ArrayField(models.TextField(), blank=True, null=True)

    def _str_(self):
        return self.name

