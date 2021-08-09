from django.db import models
from vechile.models import Vechile
from django.utils import timezone


class TransactionQuerySet(models.QuerySet):
    def get_transaction_for_parked_car(self, parking, vechile):
        return self.filter(parking_space=parking, vechile=vechile, exit_point__isnull=True).first()


class TransactionManager(models.Manager):

    def get_queryset(self):
        return TransactionQuerySet(self.model, using=self._db)

    def park_car_with_transaction(self, parking_id, registration_number, vechile_type, entry_point, vechile_name=''):
        from django.db import transaction
        from parking.models import Parking

        if not registration_number:
            raise Exception("Reg. no is not found")
        if not entry_point:
            raise Exception("Entry point is needed")
        parking = Parking.objects.filter(
            id=parking_id
        ).first()
        if not parking:
            raise Exception("Parking not found")

        vechile = Vechile.objects.filter(registration_no=registration_number).first()
        if not vechile:
            vechile = Vechile.objects.create(
                registration_no=registration_number,
                name=vechile_name,
                vechile_type=vechile_type
            )
        with transaction.atomic():
            space = Parking.objects.park_car(
                parking=parking,
                vechile=vechile
            )
            if not space:
                raise Exception("Parking Lot is full")
            self.create(
                parking_space=space,
                vechile=vechile,
                entry_point=entry_point
            )
            return space

    def exit_car_with_transaction(self, parking_id, registration_number, exit_point):
        from parking.models import Parking, Rate
        from django.db import transaction

        if not registration_number:
            raise Exception("Reg. no is not found")
        if not exit_point:
            raise Exception("Exit point is needed")
        parking = Parking.objects.filter(
            id=parking_id
        ).first()
        if not parking:
            raise Exception("Parking not found")

        vechile = Vechile.objects.filter(registration_no=registration_number).first()
        if not vechile:
            raise Exception("Vechile not found")


        with transaction.atomic():
            space = Parking.objects.exit_car(parking=parking, vechile=vechile)
            tran = self.all().get_transaction_for_parked_car(space, vechile)
            if not tran:
                raise Exception("Car is not parked")
            tran.exit_point = exit_point
            delta = (timezone.now() - tran.parking_time).total_seconds() / (60*60)
            price = Rate.objects.get_price_for_parked_car(
                parking=parking, vechile_type=vechile.vechile_type,
                hours=delta
            )
            tran.price = price
            tran.exit_time = timezone.now()
            tran.save()
            return space