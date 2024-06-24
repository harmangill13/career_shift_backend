from django.shortcuts import render
from .models import Career
from rest_framework import viewsets, permissions
from .serializers import CareerSerializer
# Create your views here.

class CareerViewset(viewsets.ModelViewSet):
  queryset = Career.objects.all()
  serializer_class = CareerSerializer
  permission_classes = [permissions.AllowAny]
  