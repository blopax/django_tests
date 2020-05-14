from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    template_name = 'ex00/index.html'
    return render(request, template_name)