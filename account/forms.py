from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):

        error_messages = {
            'duplicate_email': 'Email is already taken'
        }

        email = self.cleaned_data.get('email')

        try:
            User.objects.get(email=email)

            raise forms.ValidationError(
                error_messages['duplicate_email'],
                code = 'duplicate_email',
            )
        except User.DoesNotExist:
            return email
