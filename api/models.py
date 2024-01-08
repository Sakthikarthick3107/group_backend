from django.db import models

# Create your models here.

class CollegeEvents(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length = 50)
    description = models.TextField()
    seats = models.IntegerField()
    
class Register(models.Model):
    participant_id = models.AutoField(primary_key=True)
    participant_name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 50 , unique=True)
    event_id = models.IntegerField()
    
