from django.urls import path
from app1.views import *

file_name="anything"
urlpatterns = [
    path('rip/',rip,name='rip'),
    path('fruits/',fruits,name='fruits'),
]