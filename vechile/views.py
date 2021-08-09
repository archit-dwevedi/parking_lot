from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vechile
from .serializers import TransactionSerializer


class VechileDetailsAPI(APIView):

    def get(self, request):
        registration_number = request.GET.get('registration_number')
        transacts = Vechile.objects.get_vechile_details(registration_number=registration_number)
        serializer = TransactionSerializer(transacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
