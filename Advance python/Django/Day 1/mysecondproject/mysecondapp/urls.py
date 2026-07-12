from django.urls import path
from . import views

urlpatterns = [
    path('greet/', views.greet, name='greet'),
    path('add/', views.add, name='add'),
    path('sub/', views.sub, name='sub'),
    path('mul/', views.mul, name='mul'),
    path('div/', views.div, name='div')
]