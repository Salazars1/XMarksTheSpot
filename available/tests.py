from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
# Create your tests here.
class AvailablePageTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_AvailablePage(self):
        c = Client()
        response = c.post('/login/', {'username': 'testuser', 'password': 'secret'})
        response = c.get('/available/')
        self.assertEqual(response.status_code, 200)
