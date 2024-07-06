from django.urls import path
from ipl.views import *

app_name="ipl"

urlpatterns=[
     path('rinky/',rinky,name='rinky')
]