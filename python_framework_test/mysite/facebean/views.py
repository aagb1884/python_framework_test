from django.http import HttpResponse
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the facebean index.")

class MessageViewset(viewsets.ModelViewSet):
    queryset= Message.objects.all()
    serializer_class = MessageSerializer