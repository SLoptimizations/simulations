from django.contrib import admin
from django.urls import path
from simulation1 import views

urlpatterns = [
    # path('', views.AboutView.as_view(), name='about'),
    path('', views.register, name='about'),
]
