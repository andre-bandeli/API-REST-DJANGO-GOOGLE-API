from django.shortcuts import render
from django.contrib.auth import logout


def home(request):
    return render(request, 'index.html')

def logout_v(request):
    logout(request)