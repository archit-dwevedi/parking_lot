from rest_framework import serializers

# Import models
from transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'parking_space_id', 'parking_time', 'exit_time', 'entry_point', 'exit_point', 'price']

    def create(self, validated_data):
        pass
