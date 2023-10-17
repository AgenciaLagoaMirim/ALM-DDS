from django.urls import path

from .views import new_reading

urlpatterns = [
    path("readings", new_reading, name="readings"),
]
