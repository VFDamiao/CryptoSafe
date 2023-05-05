from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Vault

def home(request):
  return render(request, 'home/index.html')

@login_required
def vault(request):
  user = request.user.id
  vaults = Vault.objects.filter(user_id=user)
  return render(request, 'vault/index.html', {'vaults': vaults})

@login_required
def create_vault(request):

  if request.method == 'POST':
    name = request.POST.get('name')
    description = request.POST.get('description')
    user_id = request.user.id

    vault = Vault(name=name, description=description, user_id=user_id)
    vault.save()
    
    return redirect('vault')
  else:
    return redirect('vault')

@login_required
def delete_vault(request, vault_id):
  vault = Vault.objects.get(id=vault_id)
  vault.delete()
  return redirect('vault')


@login_required
def edit_vault(request, vault_id):
  vault = Vault.objects.get(id=vault_id)
  return render(request, 'vault/edit.html', {'vault': vault})


@login_required
def update_vault(request, vault_id):
  vault = get_object_or_404(Vault, id=vault_id)

  if request.method == 'POST':
    vault.name = request.POST.get('name')
    vault.description = request.POST.get('description')
    vault.save()
    return redirect('edit_vault', vault_id=vault_id)
  else:
    return redirect('edit_vault', vault_id=vault_id)