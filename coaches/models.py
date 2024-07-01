from django.db import models

class Coach(models.Model):
  name = models.CharField(max_length=100)
  field = models.CharField(max_length=100)
  bio = models.CharField(max_length=500)
  gender = models.CharField(max_length=100)
  image = models.URLField(max_length=200, null=True, blank=True)
# Create your models here.
