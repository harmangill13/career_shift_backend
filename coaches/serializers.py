from .models import Coach
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class CoachSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Coach
    fields = ['id', 'name', 'field', 'bio', 'gender', 'image']