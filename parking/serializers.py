from rest_framework import serializers


class ParkSerializer(serializers.Serializer):
    parking_id = serializers.IntegerField(min_value=1, write_only=True)
    registration_number = serializers.CharField(max_length=255, write_only=True)
    vechile_type = serializers.CharField(max_length=255, write_only=True)
    entry_point = serializers.CharField(max_length=25, write_only=True)
    vechile_name = serializers.CharField(max_length=255, allow_null=True, write_only=True, required=False)
    success = serializers.CharField(max_length=25, read_only=True)

    def create(self, validated_data):
        from transaction.models import Transaction
        Transaction.objects.park_car_with_transaction(
            **validated_data
        )
        return True

    def update(self, instance, validated_data):
        pass


class ExitSerializer(serializers.Serializer):
    parking_id = serializers.IntegerField(min_value=1, write_only=True)
    registration_number = serializers.CharField(max_length=255, write_only=True)
    exit_point = serializers.CharField(max_length=25, write_only=True)
    success = serializers.CharField(max_length=25, read_only=True)

    def create(self, validated_data):
        from transaction.models import Transaction
        space = Transaction.objects.exit_car_with_transaction(
            **validated_data
        )
        return True

    def update(self, instance, validated_data):
        pass
