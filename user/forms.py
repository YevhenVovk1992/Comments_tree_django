from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='User name',
        widget=forms.TextInput(attrs={"placeholder": "Login", "class": "input is-large"})
    )
    email = forms.CharField(
        label='User name',
        widget=forms.TextInput(attrs={"placeholder": "Email", "class": "input is-large"})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "input is-large"}),
    )
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={"placeholder": "Repeat password", "class": "input is-large"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(
        label='User name',
        widget=forms.TextInput(attrs={"placeholder": "Login", "class": "input is-large"})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "input is-large"}),
    )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']