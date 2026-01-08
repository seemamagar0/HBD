from django.shortcuts import render
from django.utils import timezone

def happy_birthday(request):
    context = {
        "name": "Dost 🎉",   # Change name if you want
        "today": timezone.now().date(),
    }
    return render(request, "hbd.html", context)
