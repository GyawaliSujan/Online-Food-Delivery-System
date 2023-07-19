from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=10, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=10, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']