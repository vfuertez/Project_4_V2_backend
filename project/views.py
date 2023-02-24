from django.shortcuts import render

# Create your views here.
from .models import Proj
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProjSerializer

class ProjViewset(viewsets.ModelViewSet):
    queryset = Proj.objects.all()
    serializer_class = ProjSerializer
    permission_classes = [permissions.AllowAny]