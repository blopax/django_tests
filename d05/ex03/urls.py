from django.urls import path

from . import views

urlpatterns = [
    path('populate', views.populate, name='ex03-populate'),
    path('display', views.display, name='ex03-display'),
    path('remove', views.remove, name='ex03-remove'),
    path('update', views.update, name='ex03-update')
]