from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_metrics, name='calculate_metrics'),
]
