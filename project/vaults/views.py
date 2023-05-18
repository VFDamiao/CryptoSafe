from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from cryptography.fernet import Fernet

from .models import Vault, Credential

key = b'PmIJ9VS5ikwe0YFCced8rqQzU0UBeKn4shkyxXL_PJU='

fernet = Fernet(key)

def encrypt(text):
  encoded_text = text.encode()
  encrypted_text = fernet.encrypt(encoded_text)

  return encrypted_text.decode("utf-8")

def decrypt(encrypted_text):
  decoded_text = encrypted_text.encode("utf-8")
  decrypted_text = fernet.decrypt(decoded_text)


  return decrypted_text.decode()


def home(request):
  return render(request, 'home/index.html')

@login_required
def vault(request):
  user_id = request.user.id
  vaults = Vault.objects.filter(user_id=user_id)

  user = request.user

  return render(request, 'vault/index.html', {'vaults': vaults, 'user': user})

@login_required
def create_vault(request):

  if request.method == 'POST':
    name = request.POST.get('name')
    user_id = request.user.id

    vault = Vault(name=name, user_id=user_id)
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
    vault.save()
    return redirect('vault')
  else:
    return redirect('vault')
  
@login_required
def my_profile(request):
  user = request.user.id

  return render(request, 'vault/my_profile.html', {'user': user})


@login_required
def credential(request, vault_id):
  credentials = Credential.objects.filter(vault_id=vault_id)
  vault = Vault.objects.get(id=vault_id)
  user = request.user

  for credential in credentials:
    credential.password = decrypt(credential.password)

  return render(request, 'vault/credential.html', {'vault': vault, 'credentials': credentials, 'user':user})


@login_required
def create_credential(request, vault_id):
  if request.method == 'POST':
    name = request.POST.get('name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    description = request.POST.get('description')
    user = request.user.id
    vault = vault_id

    encrypt_password = encrypt(password)

    credential = Credential(name=name, username=username, password=encrypt_password, description=description, user_id=user, vault_id=vault)
    credential.save()
    
    return redirect('credential', vault_id)
  else:
    return redirect('credential', vault_id)
  
@login_required
def delete_credential(resquest, credential_id):
  credential = Credential.objects.get(id=credential_id)
  vault_id = credential.vault_id
  credential.delete()

  return redirect('credential', vault_id)

@login_required
def update_credential(request, credential_id):
  credential = get_object_or_404(Credential, id=credential_id)

  if request.method == 'POST':
    credential.name = request.POST.get('name')
    credential.username = request.POST.get('username')
    credential.password = request.POST.get('password')
    credential.description = request.POST.get('description')

    credential.password = encrypt(credential.password)

    credential.save()
    return redirect('credential', credential.vault_id)
  else:
    return redirect('credential', credential.vault_id)