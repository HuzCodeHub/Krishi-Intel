from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput,EmailInput
from django.core.exceptions import ValidationError
from .models import CustomUser


class UserAdminCreationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and email.endswith('@gmail.com'):
            raise ValidationError("Gmail addresses are not allowed.")
        return email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and email.endswith('@yahoo.in'):
            raise ValidationError("Yahoo addresses are not allowed.")
        return email


    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2','company_name',
                  'role','first_name','last_name']


def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        CustomUser.email = self.cleaned_data['email']
       
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
 
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'] = self.fields['email']
        del self.fields['username']
 
    password = forms.CharField(widget=PasswordInput(
        attrs={'placeholder': 'Password'}))
        
