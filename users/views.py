from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from django.db.utils import IntegrityError

from users.forms import *
from users.models import *


class RegisterFormView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = 'CarpetShops/add-shop.html'

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        users = User.objects.filter(username=username)
        if users:
            return render(self.request, self.template_name, {"error": True, "username_unavailable": True})
        else:
            user = User(username=username, first_name=first_name, last_name=last_name, password=password,
                        email=email, phone_number=phone_number, user_type=UserType.carpet_cleaning_owner)
            user.set_password(password)
            try:
                user.save()
            except IntegrityError:
                return render(self.request, self.template_name, {"error": True, "duplicate_phone_number": True})
            return redirect(reverse("add-shop"))
