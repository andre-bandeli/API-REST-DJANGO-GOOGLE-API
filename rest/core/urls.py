
from re import template
from django.urls import path

from .views import home as v


urlpatterns = [
    path('', v, name="index"),
]
