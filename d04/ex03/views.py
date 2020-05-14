from django.shortcuts import render

# Create your views here.

def shades(request):
    template_name = 'ex03/index.html'
    shades = [x for x in range(256)]
    return render(request, template_name, {'shades': shades})