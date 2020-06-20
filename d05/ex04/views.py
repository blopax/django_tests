from django.shortcuts import render

# Create your views here.

from .models.people import People 

def display(request):
    people_list = None
    people_list = People.objects.order_by('name').filter(homeworld__climate__contains='windy').values('name', 'homeworld', 'homeworld__climate')
    return render(request, 'ex04/display.html', {'people_list':people_list})