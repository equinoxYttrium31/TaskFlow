from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.hello_world),  # Maps the URL to the view function
]