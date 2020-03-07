from django.db import models

# Create your models here.

class cricketApi(models.Model):
    data = models.TextField(max_length=1000)
    created = models.DateField(auto_now= True)
    
    
class Match(models.Model):
    pass