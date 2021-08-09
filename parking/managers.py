from django.db import models


class ParkingQuerySet(models.QuerySet):

    def get_empty_parking_space(self, parking, vechile_type):
        from .models import ParkingSpace
        return ParkingSpace.objects.filter(
            parking=parking,
            vechile_type=vechile_type,
            parked_car__isnull=True
        ).first()

    def get_parked_car_space(self, parking, vechile):
        from .models import ParkingSpace
        return ParkingSpace.objects.filter(parking=parking, parked_car=vechile).first()


class ParkingManager(models.Manager):
    def get_queryset(self):
        return ParkingQuerySet(self.model, using=self._db)

    def park_car(self, parking, vechile):
        if not parking:
            raise Exception("Parking not found")
        if not vechile:
            raise Exception("Vechile is not found")

        parked_space = self.all().get_parked_car_space(parking, vechile)
        if parked_space:
            raise Exception("Car is already parked")
        space = self.all().get_empty_parking_space(parking, vechile.vechile_type)
        if not space:
            raise Exception("No Parking spots are empty")

        space.parked_car = vechile
        space.save()
        return space

    def exit_car(self, parking, vechile):
        if not parking:
            raise Exception("Parking not found")
        if not vechile:
            raise Exception("Vechile is not found")

        parked_space = self.all().get_parked_car_space(parking, vechile)
        if not parked_space:
            raise Exception("Car is not parked")

        parked_space.parked_car = None
        parked_space.save()
        return parked_space


class RateManager(models.Manager):

    def get_price_for_parked_car(self, parking, vechile_type, hours):
        rate = self.filter(
            parking=parking,
            vechile_type=vechile_type,
            start_hours__lte=hours,
            end_hours__gte=hours
        ).first()
        if not rate:
            return 100
        return rate.price
