# from django.http import Http404
# from django.template import loader
from rest_framework import viewsets, status
from .models import Message
from .serializers import MessageSerializer

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


def index(request):
    latest_message_list = Message.objects.order_by("pub_date")[:5]
    context = {
        "latest_message_list": latest_message_list,
    }
    return render(request, "facebean/index.html", context)


class MessageViewset(viewsets.ModelViewSet):
    queryset= Message.objects.all()
    serializer_class = MessageSerializer

@api_view(['GET', 'POST', 'DELETE'])
def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        
        id = request.query_params.get('id', None)
        if id is not None:
            messages = messages.filter(id__icontains=id)
        
        messages_serializer = MessageSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        message_data = JSONParser().parse(request)
        message_serializer = MessageSerializer(data=message_data)
        if message_serializer.is_valid():
            message_serializer.save()
            return JsonResponse(message_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Message.objects.all().delete()
        return JsonResponse({'message': '{} Messages were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def message_detail(request, pk):
    try: 
        message = Message.objects.get(pk=pk) 
    except Message.DoesNotExist: 
        return JsonResponse({'message': 'The message does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        message_serializer = MessageSerializer(message) 
        return JsonResponse(message_serializer.data) 
 
    elif request.method == 'PUT': 
        message_data = JSONParser().parse(request) 
        message_serializer = MessageSerializer(message, data=message_data) 
        if message_serializer.is_valid(): 
            message_serializer.save() 
            return JsonResponse(message_serializer.data) 
        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        message.delete() 
        return JsonResponse({'message': 'Message was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def message_list_published(request):
    messages = Message.objects.filter(published=True)
        
    if request.method == 'GET': 
        message_serializer = MessageSerializer(messages, many=True)
        return JsonResponse(message_serializer.data, safe=False)