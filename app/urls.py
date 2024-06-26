from django.urls import path
from app.views import *

file_name="anything"
urlpatterns = [
    path('planet/',planet,name='planet'),
    path('person/',person,name='person'),
]