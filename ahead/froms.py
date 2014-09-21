# -*- coding: utf-8 -*-
from corntib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    username = forms.RegexField(label=_("Username"), max_length=30, min_length=4,
        regex=r'^\w+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "_ characters.")})


    username = forms.RegexField(max_length=30, min_length=6)