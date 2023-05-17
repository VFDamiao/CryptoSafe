from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('client/vault/', views.vault, name='vault'),
    path('client/create_vault/', views.create_vault, name='create_vault'),
    path('client/delete_vault/<int:vault_id>/', views.delete_vault, name='delete_vault'),
    path('client/edit_vault/<int:vault_id>/', views.edit_vault, name='edit_vault'),
    path('client/update_vault/<int:vault_id>/', views.update_vault, name='update_vault'),
    path('client/my-profile/', views.my_profile, name='my_profile'),
    path('client/credential/<int:vault_id>/', views.credential, name='credential'),
    path('client/create_credential/<int:vault_id>/', views.create_credential, name='create_credential'),
    path('client/delete_credential/<int:credential_id>/', views.delete_credential, name='delete_credential'),
    path('client/update_credential/<int:credential_id>/', views.update_credential, name='update_credential'),
]