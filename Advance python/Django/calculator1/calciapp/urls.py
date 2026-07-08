from django.urls import path
from . import views

urlpatterns = [
    path('greet/', views.greet, name='greet'),
    path('getadditionpage/', views.getadditionpage, name='getadditionpage'),
    path('addition/', views.addition, name='addition'),

    path('getsubpage/', views.getsubpage , name="getsubpage"),
    path('sub/', views.sub, name='sub'),

    path('getmulpage/', views.getmulpage , name="getmulpage"),
    path('mul/', views.mul, name='mul'),

    path('getdivpage/', views.getdivpage , name="getdivpage"),
    path('div/', views.div, name='div'),

    path('getfloordivpage/', views.getfloordivpage , name="getfloordivpage"),
    path('floordiv/', views.floordiv, name='floordiv'),
]