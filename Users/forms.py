from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import re


def strong_password(password):
     regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
 
     if not regex.match(password):
         raise ValidationError((
             'Password must have at least one uppercase letter, one number and at least 8 characters.'
         ),
             code='invalid'
         )
         
def valid_username(username):
    regex = re.compile(r'^[\w.@+-]{6,18}$')

    if not regex.match(username):
        raise ValidationError((
                'Username must be 6-18 characters long and contain only letters, numbers, and @/./+/-/_ characters.',
        ),
            code='invalid'
        )

class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'placeholder': 'Type your username',
            'required': 'required',
            'minlength': 6,
            'maxlength': 18
        }),
        help_text=(
            'Username must be 6-18 characters long and contain only letters, numbers, and @/./+/-/_ characters.'
        ),
        validators=[valid_username]
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type your password',
            'required': 'required'
        }),
        help_text=(
            'Password must have at least one uppercase letter, one number and at least 8 characters.'
        ),
        validators=[strong_password]
    )
    
    repeat_password = forms.CharField(
        required=True,
        label='repeat_password',
        widget=forms.PasswordInput(attrs={
            'label': 'Repeat password',
            'placeholder': 'Repeat your password',
            'required': 'required'
        })
    )
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        error_messages = {
            'username': {
                'required': 'This field cannot be empty',
                'invalid': 'This cannot be invalid'
            }
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Type your username',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Type your best email',
                'required': 'required'
            }),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        
        if password != repeat_password:
            raise ValidationError({
                'password': 'Passwords do not match.',
                'repeat_password': 'Passwords do not match.'
            })