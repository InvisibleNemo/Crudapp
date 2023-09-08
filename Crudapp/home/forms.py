# home/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your custom user model

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ['username',
                  'password1', 
                  'password2', 
                  'email',
                  'first_name',
                  'last_name',
                  'phone',
                  'address',
                  'city',
                  'state',                  
                  'profile_picture', 
                  ]
