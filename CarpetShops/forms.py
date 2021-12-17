from django import forms


class RegisterForm(forms.Form):
    owner_username = forms.CharField()
    name = forms.CharField()
    opens_at = forms.TimeField()
    closes_at = forms.TimeField()
    address = forms.CharField()
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    delivery_cost = forms.IntegerField()
