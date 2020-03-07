from rest_framework import serializers
from api.models import cricketApi


class CricketApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = cricketApi
        fiels = ('__all__')
        
        