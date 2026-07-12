from django.urls import path
from . import views 

urlpatterns = [
    path('getsigninpage/', views.getsigninpage, name="getsigninpage"),
    path('signin', views.signin, name='signin')
]