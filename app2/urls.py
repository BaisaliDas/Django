from django.urls import path
from app2.views import *

file_name="anything"
urlpatterns = [
    path('admin/',admin,name='admin'),
    path('admin2/',admin2,name='admin2'),
    path('jinja_print/',jinja_print,name='jinja_print'),
    path('jinja_operation/',jinja_operation,name='jinja_operation'),
]