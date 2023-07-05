from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('les', index_2)
]
