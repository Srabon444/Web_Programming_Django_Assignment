from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'business/index.html')


def payment(request):
    return render(request, 'business/payment.html')


def login(request):
    return render(request, 'business/login.html')
