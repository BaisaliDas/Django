from django.urls import path
from app.views import *

app_name="check"

urlpatterns=[
     path('sachivji/',sachivji,name='sachivji'),
]