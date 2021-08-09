from django.db import models

from parking.models import Parking, ParkingSpace
from transaction.managers import TransactionManager
from vechile.models import Vechile


class Transaction(models.Model):
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.DO_NOTHING, db_column='parking_space_id')
    vechile = models.ForeignKey(Vechile, on_delete=models.DO_NOTHING, db_column='vechile_id')
    parking_time = models.DateTimeField(auto_now_add=True, db_column='start_time')
    exit_time = models.DateTimeField(null=True, blank=True, db_column='exit_time')
    price = models.DecimalField(max_digits=25, decimal_places=2, null=True, db_column='price')
    entry_point = models.CharField(max_length=255, db_column='entry_point')
    exit_point = models.CharField(max_length=255, null=True, db_column='exit_point')

    objects = TransactionManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'transaction'
