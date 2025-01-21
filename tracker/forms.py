# forms.py
from django import forms
from .models import Budget
from django import forms
from .models import Income
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'category', 'amount', 'expense']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Budget Name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'expense': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Expense'}),
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source']

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        help_text='A valid email address is required.',
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create a password'}),
        help_text='Your password must be at least 8 characters long.',
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        help_text='Enter the same password for verification.',
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
