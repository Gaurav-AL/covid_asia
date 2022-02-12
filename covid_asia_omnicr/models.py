from pyexpat import model
from django.db import models
import datetime

# Create your models here.

class Asia(models.Model):
    Date = models.DateField(max_length=100,default=datetime.datetime.now().date())
    Time = models.TimeField(default=datetime.datetime.now().time())
    Countries = models.CharField(max_length=100)
    Confirmed = models.CharField(max_length=100)
    Recovered = models.CharField(max_length=100)
    Deaths = models.CharField(max_length=100)
    Active_today = models.CharField(max_length=100)
    Death_today = models.CharField(max_length=100)
    Recovered_today = models.CharField(max_length=100)


