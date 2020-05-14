from django.shortcuts import render

# Create your views here.

def django(request):
    return render(request, 'ex01/django.html', {'styles':"static/ex01/style1.css"})

def affichage(request):
    return render(request, 'ex01/affichage.html', {'styles':"static/ex01/style1.css"})

def templates(request):
    return render(request, 'ex01/templates.html', {'styles':"static/ex01/style1.css"})