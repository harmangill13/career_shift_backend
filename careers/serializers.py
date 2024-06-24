from .models import Career
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class CareerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Career
    fields = ['id', 'name', 'description', 'requirements', 'resources']