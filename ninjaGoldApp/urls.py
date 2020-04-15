from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('processMoney', views.processMoney),
    path('reset', views.reset)
]
