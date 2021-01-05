from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import  reverse_lazy
from .forms import SignUpForm
# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class= SignUpForm
    template_name = 'registration/register.html'
    success_url=reverse_lazy('login')

class UserEditView(generic.CreateView):
        form_class = UserChangeForm
        template_name = 'registration/edit.html'
        success_url = reverse_lazy('home')

def get_object(self):
        return self.request.user
