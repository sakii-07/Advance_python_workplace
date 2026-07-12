from django.urls import path
from . import views

urlpatterns = [
    path('getaddpage/', views.getaddpage, name='getaddpage'),
    path('add/', views.add, name='add')
]
