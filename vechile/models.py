from django.db import models

from vechile.choices import VechileTypeChoices
from vechile.managers import VechileManager


class Vechile(models.Model):
    registration_no = models.CharField(max_length=255, db_column='registration_no')
    name = models.CharField(max_length=255, null=True, blank=True, db_column='name')
    vechile_type = models.CharField(max_length=25, choices=VechileTypeChoices.CHOICES, db_column='vechile_type')

    objects = VechileManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vechile'
