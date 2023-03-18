from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('client/vault/', views.vault, name='vault'),
]