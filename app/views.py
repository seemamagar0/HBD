from django.shortcuts import render

# Create your views here.
from django.utils import timezone

def happy_birthday(request):
    # Example: you can fetch user from DB later
    context = {
        "name": "Syaanuuu💗",
        "today": timezone.now().date(),
    }
    return render(request, "hbd.html", context)
