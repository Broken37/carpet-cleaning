from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField()
