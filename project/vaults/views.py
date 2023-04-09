from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
  return render(request, 'home/index.html')

@login_required
def vault(request):
  return render(request, 'vault/index.html')