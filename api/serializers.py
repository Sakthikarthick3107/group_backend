from rest_framework import serializers
from .models import CollegeEvents , Register


class CollegeEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CollegeEvents
        fields = '__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
    