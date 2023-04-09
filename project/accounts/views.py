from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Nome', max_length=30)
    email = forms.CharField(label='Email', max_length=30)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'email', )

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'