from django.urls import path

from . import views

urlpatterns = [
    path('', views.django_form, name='django_form')
]