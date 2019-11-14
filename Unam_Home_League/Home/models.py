from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Log_Standing(models.Model):    
    Position = models.IntegerField(max_length=200, blank=False)
    Team = models.CharField(max_length=200, blank=False)
    GP = models.IntegerField(max_length=200, blank=False)       
    W = models.IntegerField(max_length=200, blank=False)
    D = models.IntegerField(max_length=200, blank=False)
    L = models.IntegerField(max_length=200, blank=False)
    GF = models.IntegerField(max_length=200, blank=False)
    GA = models.IntegerField(max_length=200, blank=False)
    GD = models.IntegerField(max_length=200, blank=False)
    PTS = models.IntegerField(max_length=200, blank=False)  
   

    
    def __str__(self):
        return self.Team

class PlayersDetails(models.Model):
    Team = models.CharField(max_length=200, blank=False)
    Name = models.CharField(max_length=200, blank=False)       
    Surname = models.CharField(max_length=200, blank=False)
    Student_Number = models.CharField(max_length=200, blank=False)
    Institution = models.CharField(max_length=200, blank=False) 
   

    def __str__(self):
        return self.Name

    
class Fixtures(models.Model):    
    Home = models.CharField(max_length=200, blank=False)       
    VS = models.CharField(max_length=200, blank=False)
    Away = models.CharField(max_length=200, blank=False)
    Stadium = models.CharField(max_length=200, blank=False)
    start_datetime = models.DateTimeField( null=True, blank=True) 
   

    
    def __str__(self):
        return self.Stadium

class Results(models.Model):    
    Home = models.CharField(max_length=200, blank=False)       
    Score = models.CharField(max_length=200, blank=False)
    Away = models.CharField(max_length=200, blank=False)
    start_datetime = models.DateTimeField(null=True, blank=True)
         
    def __str__(self):
        return self.Home
      
class Contact(models.Model):
    full_name = models.CharField(max_length=20)  
    email  = models.EmailField(max_length=30)
    subject  = models.CharField(max_length=30)
    message  = models.TextField()  
    class Meta:  
        db_table = "contact"  

    def __str__(self):
        return self.subject