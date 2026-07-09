from django.urls import path
from . import views

urlpatterns = [
    path('getaddpage/', views.getaddpage, name='getaddpage'),
    path('add/', views.add, name='add'),

    path('getsubpage/', views.getsubpage, name='getsubpage'),
    path('sub/', views.sub, name='sub'),

    path('getmulpage/', views.getmulpage, name='getmulpage'),
    path('mul/', views.mul, name='mul'),

    path('getdivpage/', views.getdivpage, name='getdivpage'),
    path('div/', views.div, name='div'),

    path('getfloordivpage/', views.getfloordivpage, name='getfloordivpage'),
    path('floordiv/', views.floordiv, name='floordiv')
]
