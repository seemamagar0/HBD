from django.urls import path
from .views import happy_birthday

urlpatterns = [
    path("happy-birthday/", happy_birthday, name="happy_birthday"),
]
