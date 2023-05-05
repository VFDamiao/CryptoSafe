from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

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

      exemplo = Vault(name=name, description=description, user_id=user_id)
      exemplo.save()
      
      return redirect('vault')
  else:
      return redirect('vault')

def delete_vault(request, vault_id):
  vault = Vault.objects.get(id=vault_id)
  vault.delete()
  return redirect('vault')