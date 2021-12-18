from django import forms
from django.core.validators import RegexValidator


class RegisterForm(forms.Form):
    USER_TYPE = (
        (1, "customer"),
        (2, "carpet_cleaning_owner")
    )
    phone_regex = RegexValidator(
        regex=r"^(09)\d{9}$",
        message="phone_number format: 09xxxxxxxxx",
    )

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(validators=[phone_regex])
    user_type = forms.ChoiceField(choices=USER_TYPE, label="", initial=1, widget=forms.Select(), required=True)
