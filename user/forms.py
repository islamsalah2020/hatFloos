from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    FB = forms.URLField(required=False, max_length=60)
    DOB = forms.DateTimeField(required=False)
    picture = forms.ImageField(required=True)
    country = forms.CharField(required=False, max_length=20)
    phone = forms.RegexField(regex=r'^01[0125][0-9]{8}$')

    class Meta(UserCreationForm):
        model = CustomUser

        fields = (
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'FB', 'DOB', 'country', 'phone',
            'picture')


class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    FB = forms.URLField(required=False, max_length=60)
    DOB = forms.DateTimeField(required=False)
    picture = forms.ImageField(required=False)
    country = forms.CharField(required=False, max_length=20)
    phone = forms.RegexField(regex=r'^01[0125][0-9]{8}$')

    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password', 'FB', 'DOB', 'country', 'phone',
            'picture')


class ReportForm(forms.Form):
    report_reason = forms.CharField(max_length=100)

