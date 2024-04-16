from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, STATE_CHOICES



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)  # Add first name field
    last_name = forms.CharField(max_length=30) 
    email = forms.EmailField(required=True)  # Add email field
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerProfileForm(forms.ModelForm):
    state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone','locality', 'city', 'state']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
