from django.shortcuts import render
from .models import Student


def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def about(request):
    return render(request, 'home.html', {'name': 'about'})


def contact(request):
    return render(request, 'home.html', {'name': 'contact'})
