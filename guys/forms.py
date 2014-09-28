# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django import forms

from .models import User


class RegisterForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
        'duplicate_email': _("A user with that email already exists."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30, min_length=4,
        regex=r'^\w+$',
        help_text=_("4 - 30 characters. Letters, digits and "
                    "_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "_ characters.")})

    password1 = forms.CharField(label=_("Password"), min_length=6)
    password2 = forms.CharField(label=_("Password"), min_length=6)
    id = forms.IntegerField(widget=forms.widgets.HiddenInput())


    class Meta:
        model = User
        fields = ("username", "email")


    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user