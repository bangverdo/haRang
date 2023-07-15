from django.db import models

# Create your models here.
class Bus(models.Model):
    num = models.CharField(max_length=100)
    min = models.CharField(max_length=100)
    congestion = models.CharField(max_length=100)