from django.db import models
import datetime



# Create your models here.
class Countries(models.Model):
    aid = models.IntegerField(primary_key=True)
    Country = models.CharField(max_length=100)

    

class CumulativeStats(models.Model):
    aid = models.IntegerField(primary_key=True)
    Confirmed = models.CharField(max_length=100)
    Recovered = models.CharField(max_length=100)
    Deaths = models.CharField(max_length=100)

    


class DeltaStats(models.Model):
    aid = models.IntegerField(primary_key=True)
    Date = models.DateField(max_length=100,default=datetime.datetime.now().date())
    Time = models.TimeField(default=datetime.datetime.now().time())
    Active = models.CharField(max_length=100,default="0")
    Death = models.CharField(max_length=100,default="0")
    Recovered = models.CharField(max_length=100,default="0")

    


