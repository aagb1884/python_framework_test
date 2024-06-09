from rest_framework import viewsets, status
from .models import Message
from .serializers import MessageSerializer

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        context = {
            "message_list": messages,
        }
        return render(request, "facebean/index.html", context)
        
    elif request.method == 'POST':
        message_data = JSONParser().parse(request)
        message_serializer = MessageSerializer(data=message_data)
        if message_serializer.is_valid():
            message_serializer.save()
            return JsonResponse(message_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
