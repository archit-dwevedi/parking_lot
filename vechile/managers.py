from django.db import models


class VechileManager(models.Manager):

    def get_vechile_details(self, registration_number):
        from transaction.models import Transaction
        if not registration_number:
            raise Exception("Registration number not found")

        vechile = self.filter(registration_no=registration_number).first()
        if not vechile:
            raise Exception("Vechile not found")

        return Transaction.objects.filter(vechile=vechile)

