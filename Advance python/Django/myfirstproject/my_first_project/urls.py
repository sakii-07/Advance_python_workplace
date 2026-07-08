from django.urls import path
from . import views

urlpatterns = [
    path("my_first_project/",views.Greet, name = "greet")
]