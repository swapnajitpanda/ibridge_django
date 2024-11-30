
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('show_data/', views.show_data)
]