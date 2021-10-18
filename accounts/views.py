from django.shortcuts import render
from . import forms
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class SignUp(CreateView):
    template_name = 'accounts/signup.html'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login.html')