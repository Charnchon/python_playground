from django.urls import path
from . import views

urlpatterns = [
    path('donuts/', views.donuts, name='donuts'),
]