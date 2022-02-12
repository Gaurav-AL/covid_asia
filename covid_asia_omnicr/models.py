from pyexpat import model
from django.db import models
import datetime



# Create your models here.
class Countries(models.Model):
    aid = models.IntegerField(primary_key=True)
    Country = models.CharField(max_length=100)

    def __sizeof__(self) -> int:
        return super().__sizeof__()

class CumulativeStats(models.Model):
    aid = models.ForeignKey(Countries,on_delete=models.DO_NOTHING)
    Confirmed = models.CharField(max_length=100)
    Recovered = models.CharField(max_length=100)
    Deaths = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()


class DeltaStats(models.Model):
    aid = models.ForeignKey(Countries, on_delete=models.DO_NOTHING)
    Date = models.DateField(max_length=100,default=datetime.datetime.now().date())
    Time = models.TimeField(default=datetime.datetime.now().time())
    Active = models.CharField(max_length=100,default="0")
    Death = models.CharField(max_length=100,default="0")
    Recovered = models.CharField(max_length=100,default="0")

    def __str__(self) -> str:
        return super().__str__()


