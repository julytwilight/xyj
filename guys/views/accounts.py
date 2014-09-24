# -*- coding: utf-8 -*-
from django.views.generic import View

from ahead.utils.lazy import *
from ..forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "registration/login.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass

        return render(request, "registration/login.html", {'form': form})