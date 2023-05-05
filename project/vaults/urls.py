from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('client/vault/', views.vault, name='vault'),
    path('client/create_vault/', views.create_vault, name='create_vault'),
    path('client/delete_vault/<int:vault_id>/', views.delete_vault, name='delete_vault'),
    path('client/edit_vault/<int:vault_id>/', views.edit_vault, name='edit_vault'),
    path('client/update_vault/<int:vault_id>/', views.update_vault, name='update_vault'),
]