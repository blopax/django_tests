from django.shortcuts import render
from django.shortcuts import HttpResponse, render
from django.contrib.auth import authenticate, login


from d06.settings import NAMES
import random
from ex.forms import UserRegistrationForm


# Create your views here.


def home(request):
    if not request.session.get('username'):
        index = random.randint(0, 9)
        request.session['username'] = NAMES[index]
        request.session.set_expiry(42)
    return render(request, 'ex/index.html', {'username': request.session.get('username')})


def login(request):
    return render(request, 'ex/login.html')

def register(request):
    form = UserRegistrationForm()
    return render(request, 'ex/register.html', {"form": form})