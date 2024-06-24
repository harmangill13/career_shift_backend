from django.shortcuts import render
from .models import Coach
from rest_framework import viewsets, permissions
from .serializers import CoachSerializer
# Create your views here.

class CoachViewset(viewsets.ModelViewSet):
  queryset = Coach.objects.all()
  serializer_class = CoachSerializer
  permission_classes = [permissions.AllowAny]
  