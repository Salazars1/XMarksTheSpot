from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import Building, Room, Floor, Reservation
# Create your tests here.
class BuildingPageTest(TestCase):
    def setUp(self):
        b = Building(name = 'Alter')
        b.save()
        i = 0
        while i < 4:
            f = Floor(name = i, building = b)
            f.save()
            index = 1
            while index < 11:
                r = Room(name = index, floor = f)
                r.save()
                index += 1
            i += 1
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_BuildingPage(self):
        c = Client()
        response = c.post('/login/', {'username': 'testuser', 'password': 'secret'})
        response = c.get('/buildings/')
        self.assertEqual(response.status_code, 200)
