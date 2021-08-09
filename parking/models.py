from django.db import models

from parking.managers import ParkingManager, RateManager
from vechile.choices import VechileTypeChoices
from vechile.models import Vechile


class Parking(models.Model):
    name = models.CharField(max_length=255, db_column='name')

    objects = ParkingManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parking'


class Rate(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, db_column='parking_id')
    vechile_type = models.CharField(max_length=25, choices=VechileTypeChoices.CHOICES, db_column='vechile_type')
    start_hours = models.IntegerField(db_column='start_hours')
    end_hours = models.IntegerField(db_column='end_hours')
    price = models.IntegerField(db_column='price')

    objects = RateManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'rate'


class ParkingSpace(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, db_column='parking_id')
    vechile_type = models.CharField(max_length=25, choices=VechileTypeChoices.CHOICES, db_column='vechile_type')
    parked_car = models.ForeignKey(Vechile, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='parked_car_id')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parking_space'
