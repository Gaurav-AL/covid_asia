from django.db import models
import datetime



# Create your models here.
# Keeping track of Countries
class Countries(models.Model):
    aid = models.AutoField(primary_key=True)
    Country = models.CharField(max_length=100, default="Not Available",null=True)

# Insertion and Updation is Done in This Table
class CumulativeStats(models.Model):
    aid = models.IntegerField(primary_key=True)
    Country = models.CharField(max_length=100, default="NA",null=True)
    Confirmed = models.CharField(max_length=100,default="NA",null=True)
    Recovered = models.CharField(max_length=100,default="NA",null=True)
    Deaths = models.CharField(max_length=100,default="NA",null=True)

    

# Only Insertion is Done in this Table
class DeltaStats(models.Model):
    Country = models.CharField(max_length=100,default="NA",null=True)
    Date = models.DateField(max_length=100,default=datetime.datetime.now().date())
    Time = models.TimeField(default=datetime.datetime.now().time())
    Latest_Confirmed = models.CharField(max_length=100,null=True,default="NA")
    Latest_Recovered = models.CharField(max_length=100,null=True,default="NA")
    Latest_Deaths = models.CharField(max_length=100,null=True,default="NA")
    Active = models.CharField(max_length=100,default="NA",null=True)
    Death = models.CharField(max_length=100,default="NA",null=True)
    Recovered = models.CharField(max_length=100,default="NA",null=True)

    


