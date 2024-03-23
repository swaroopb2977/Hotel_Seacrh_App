from .views import*
from django.urls import path,include


urlpatterns = [
    path('',home),
    path('api/get-hotels',get_hotel)
]

