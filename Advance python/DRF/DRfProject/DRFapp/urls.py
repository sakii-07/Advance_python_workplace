from django.urls import path
from . import views

urlpatterns = [
    path('adduser/', views.AddUser, name='adduser'),
    path('getuser/<str:username>/', views.GetUser, name='getuser'),
    path('updateuser/<str:username>/', views.UpdateUser, name='updateuser'),
    path('deleteuser/<str:username>/', views.DeleteUser, name='deleteuser'),
]
