from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CollegeEvents , Register
from .serializers import CollegeEventSerializer , RegisterSerializer

# Create your views here.

class CollegeEventView(APIView):
    def get(self,request):
        events = CollegeEvents.objects.all()
        serialize = CollegeEventSerializer(events , many=True)
        return Response(serialize.data)

class RegisterView(APIView):
    def post(self,request):
        entry = RegisterSerializer(data=request.data)
        if entry.is_valid():
            event = CollegeEvents.objects.get(event_id = entry.validated_data['event_id'])
            event['event_id'] -= 1
            event.save()
            entry.save()
            return Response({'message':'Registered Successfully'})
            
            
        
