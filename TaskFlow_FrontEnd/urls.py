from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('home', views.home_view, name='home_view')
]