from django.shortcuts import render
from .models import Account


def index(request):
    return render(request, 'index.html')
