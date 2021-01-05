from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'forms-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'forms-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'forms-control'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

        def __init__(self,*args,**kwargs):
            super(SignUpForm , self).__init__(*args,**kwargs)
            self.field['username'].widget.attrs['class']='form-control'
            self.field['password1'].widget.attrs['class'] = 'form-control'
            self.field['password2'].widget.attrs['class'] = 'form-control'