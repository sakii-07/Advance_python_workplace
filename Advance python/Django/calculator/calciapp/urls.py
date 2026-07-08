from django.urls import path
from . import views
urlpatterns = [
    path('greet/', views.greet, name='greet'),

    path('getadditionpage/', views.getadditionpage, name='getadditionpage'),
    path('addition/', views.addition, name='addition'),

    path('getsubstractionpage/', views.getsubstractionpage, name='getsubstractionpage'),
    path('substraction/', views.substraction, name='substraction'),

    path('getmultiplicationpage/', views.getmultiplicationpage, name='getmultiplicationpage'),
    path('multiplication/', views.multiplication, name='multiplication'),

    path('getdivisionpage/', views.getdivisionpage, name='getdivisionpage'),
    path('division/', views.division, name='division'),

    path('getfloordivisionpage/', views.getfloordivisionpage, name='getfloordivisionpage'),
    path('floordivision/', views.floordivision, name='floordivision')

]