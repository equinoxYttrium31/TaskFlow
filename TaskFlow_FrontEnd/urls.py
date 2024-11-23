from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('home', views.home_view, name='home_view'),
    path('save_user', views.save_user, name='save_user'),
    path('login', views.login_view, name='login')
]