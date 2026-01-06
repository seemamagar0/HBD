from django.urls import path
from .views import happy_birthday

urlpatterns = [
    path("", happy_birthday, name="happy_birthday"),
]
