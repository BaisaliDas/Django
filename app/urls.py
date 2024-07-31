from django.urls import path
from app.views import *

app_name="country"

urlpatterns=[
    path('australia/',australia,name='australia'),
    path('brisbane/',brisbane,name='brisbane'),
]