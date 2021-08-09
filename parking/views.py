from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from parking.serializers import ParkSerializer, ExitSerializer


class ParkCarAPIView(APIView):

    def post(self, request):
        serializer = ParkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExitCarAPI(APIView):
    def post(self, request):
        serializer = ExitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
