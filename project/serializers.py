from .models import Proj
from rest_framework import serializers

class ProjSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        model= Proj
        
        fields = ['id', 'name', 'repo1', 'repo2', 'web']