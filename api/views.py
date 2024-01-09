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
        participant = RegisterSerializer(data=request.data)
        if participant.is_valid():
            participant.save()
            specific_event = CollegeEvents.objects.get(event_id = participant.validated_data['event_id'] )
            if specific_event.seats == 0:
                return Response({'message':'No seats available for this event!'})
            else:
                specific_event.seats -= 1
                specific_event.save()
                return Response({
                    'message':'Registered Successfully',
                    'data': participant.data
                    
                    })
            
        return Response({'message':'Try again'})   
        
