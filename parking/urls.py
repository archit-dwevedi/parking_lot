from django.urls import path

from parking.views import ParkCarAPIView, ExitCarAPI

urlpatterns = [
    path('park_car/', ParkCarAPIView.as_view()),
    path('exit_car/',ExitCarAPI.as_view())
]