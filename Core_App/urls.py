from django.urls import path
from Core_App.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
]