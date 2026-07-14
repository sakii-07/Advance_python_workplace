from django.urls import path
from . import views

urlpatterns = [
    path('getsigninpage/', views.getsigninpage, name='getsigninpage'),
    path('signin/', views.signin, name='signin'),
    path('getupdatepage/', views.getupdatepage, name='getupdatepage'),
    path('showuser/', views.showuser, name='showuser'),
    path('showall/', views.showall, name='showall'),
    path('update/', views.update, name='update'),
    path('getdeletepage/', views.getdeletepage, name='getdeletepage'),
    path('delete/', views.delete, name='delete'),
    path('showUserForDelete/', views.showUserForDelete, name='showUserForDelete'),
]