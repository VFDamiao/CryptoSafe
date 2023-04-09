from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

def home(request):
  template = loader.get_template('home/index.html')
  return HttpResponse(template.render())

@login_required
def vault(request):
  template = loader.get_template('vault/index.html')
  return HttpResponse(template.render())