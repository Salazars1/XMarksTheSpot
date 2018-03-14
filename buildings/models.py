from django.db import models


# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=50)


class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.IntegerField(default=0)


class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    name = models.IntegerField(default=0)
