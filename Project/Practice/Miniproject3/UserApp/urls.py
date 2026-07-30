from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetCheckUserInfo, name='getcheckuserpage'),
    path('checkuser/', views.CheckUser, name='checkuser')
]