from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Message
from django.utils import timezone

# Create your tests here.

class MessagePostTests(APITestCase):
    def test_create_message(self):
        url = reverse('message-list')
        data = {'content': 'I cannot wait to serve my country.', 'pub_date': timezone.now(), 'username': 'Cuthbert_CW', 'avatar': 'images/cuthbert.jpg'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().content, 'I cannot wait to serve my country.')
        self.assertEqual(Message.objects.get().username, 'Cuthbert_CW')

