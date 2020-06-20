from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from d06.settings import NAMES
import random

from .forms.login_form import LoginForm
from .forms.register_form import RegisterForm
from .forms.tip_form import TipForm
from .models import Tip, TipUser, Vote

# Create your views here.


def home(request):
    username = request.COOKIES.get('username', None)
    logged_in = False
    form = TipForm()
    if username:
        logged_in = True
        if request.method == "POST":
            form = TipForm(request.POST)
        if form.is_valid():
            form.save_tip(username)
            form = TipForm()
    if username is None:
        if not request.session.get('username'):
            index = random.randint(0, 9)
            request.session['username'] = NAMES[index]
            request.session.set_expiry(42)
        username = request.session['username']
    tips = Tip.objects.all()
    return render(request, 'ex01/index.html', {'form': form, 'username': username, 'logged_in': logged_in, 'tips':tips})

def login(request):
    success = None
    if request.COOKIES.get('username', None):
        return redirect(reverse('ex01:ex01-home'))
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            success = form.login()
        if success is True:
            response = redirect(reverse('ex01:ex01-home'))
            print(form.cleaned_data['username'])
            response.set_cookie('username', form.cleaned_data['username'], max_age=3600)
            return response
    else:
        form = LoginForm()
    return render(request, 'ex01/login.html', {'form': form, 'success' : success})

def register(request):
    if request.COOKIES.get('username', None):
        return redirect(reverse('ex01:ex01-home'))
    success = None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            success = form.register()
        if success is True:
            response = redirect(reverse('ex01:ex01-home'))
            print(form.cleaned_data['username'])
            response.set_cookie('username', form.cleaned_data['username'], max_age=3600)
            return response
    else:
        form = RegisterForm()
    return render(request, 'ex01/register.html', {"form": form, 'success': success})

def logout(request):
    response = redirect(reverse('ex01:ex01-home'))
    response.delete_cookie('username')
    return response

def change_tip_meta(request):
    action = None
    if request.method == 'POST':
        action = request.POST.get('action', None)
        voter = request.COOKIES.get('username', None)
        tip_pk = request.POST.get('id', None)
    if action == 'Upvote':
        vote(voter, tip_pk, 'up')
    elif action == 'Downvote':
        vote(voter, tip_pk, 'down')
    elif action == 'Delete':
        delete(voter, tip_pk)
    return redirect(reverse('ex01:ex01-home'))

def delete(voter, tip_pk):
    try:
        user = TipUser.objects.get(username=voter)
        pk = int(tip_pk)
        tip = Tip.objects.get(pk=pk)
        if tip.auteur == user or user.has_perm('ex01.delete_tip'):
            tip.delete()
    except:
        pass

def vote(voter, tip_pk, votation):
    try:
        pk = int(tip_pk)
        tip = Tip.objects.get(pk=pk)
        voter = TipUser.objects.get(username=voter)
        voter.update_perms()
        print(voter.get_all_permissions())
        vote, _ = Vote.objects.get_or_create(voter=voter, tip=tip)
        if votation == 'up' and vote.value < 1:
            if vote.value == -1:
                tip.downvotes -= 1
            vote.value = 1
            tip.upvotes += 1
            vote.save()
            tip.save()
        elif votation == 'down' and vote.value > -1 and (tip.auteur == voter or voter.has_perm('ex01.can_downvote')):
            if vote.value == 1:
                tip.upvotes -= 1
            vote.value = -1
            tip.downvotes += 1
            vote.save()
            tip.save()
    except:
        pass
