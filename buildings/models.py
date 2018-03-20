from django.db import models


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
        floorName = str(self.floor.name)
        roomName = floorName + str(self.name)
        if self.name < 10:
            roomName = floorName + str(0) + str(self.name)
        return buildingName + " " + roomName
