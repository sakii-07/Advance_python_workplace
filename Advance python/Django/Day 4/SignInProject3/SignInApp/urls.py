from django.urls import path
from . import views

urlpatterns = [
    path('getsignpage/', views.getsignpage, name='getsignpage'),
    path('signin', views.signin, name='signin'),
]