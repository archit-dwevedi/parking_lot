from django.urls import path

from vechile.views import VechileDetailsAPI

urlpatterns = [
    path('', VechileDetailsAPI.as_view())
]