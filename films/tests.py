from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class TestFilmView(TestCase):

    def setUp(self):
        self.client.login(username="admin", password="abcd1234")
    
    def test_authetication_required(self):
        self.client.logout()
        url = reverse('flims_list')
        # 403 Forbidden
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)