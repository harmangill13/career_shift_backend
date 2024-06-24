from django.db import models

class Career(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  requirements = models.CharField(max_length=1000)
  resources = models.CharField(max_length=500)

# Create your models here.
