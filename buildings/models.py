from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.IntegerField(default=0)
    def __str__(self):
        buildingName = self.building.name
        return buildingName + " " + str(self.name)


class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    name = models.IntegerField(default=0)
    def __str__(self):
        buildingName = self.floor.building.name
        roomName = str(self.name)
        if self.floor.name == 0:
            return buildingName + " 00" + roomName
        return buildingName + " " + roomName

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time = models.DateTimeField("reserved time")
    def __str__(self):
        return str(self.room) + " " + str(self.time)
