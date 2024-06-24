from django.db import models

class Coach(models.Model):
  name = models.CharField(max_length=100)
  field = models.CharField(max_length=100)
  bio = models.CharField(max_length=500)
  gender = models.CharField(max_length=100)
# Create your models here.
