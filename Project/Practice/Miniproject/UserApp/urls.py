from django.urls import path
from . import views
urlpatterns = [
    path('checkuser/', views.CheckUser, name='checkuser'),
    path('', views.GetUserPage, name='getuserpage'),
    path('getadduserpage/', views.GetaddUserPage, name='getadduserpage'),
    path('adduser/<str:username>/', views.AddUser, name='adduser')
]