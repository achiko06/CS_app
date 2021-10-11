from django.urls import path
from . views import *

app_name = "helpcentre"

urlpatterns = [
    path('', helpcentre_home, name="helpcentre_home"),
]