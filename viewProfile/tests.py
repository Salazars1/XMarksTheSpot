from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
# Create your tests here.
class ViewProfilePageTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_ViewProfilePage(self):
        c = Client()
        response = c.post('/login/', {'username': 'testuser', 'password': 'secret'})
        response = c.get('/profile/')
        self.assertEqual(response.status_code, 200)
