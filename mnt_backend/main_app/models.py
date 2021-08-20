from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField()
    ticker = models.CharField(max_length=25)
    investmentAmount = models.IntegerField()
    tickerarray = ArrayField(ArrayField(models.CharField(max_length=25)))

    def _str_(self):
        return self.name