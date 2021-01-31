from django.urls import path, include
from .views import helloApi

urlpatterns = [
    path("hello/", helloApi),
]