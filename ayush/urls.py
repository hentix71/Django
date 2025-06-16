from django.urls import path
from . import views

# /ayush chai already vai sako
urlpatterns = [
    path('', views.all_ayush, name = 'all_ayush'),
]
