from django import forms

class Signup(forms.Form):
    fullname=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)

class Login(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)