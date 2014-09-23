# -*- coding: utf-8 -*-
from ahead.utils.lazy import *
from ..forms import RegisterForm

def default(request):
    return render(request, "index.html", {})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            return HttpResponse('Success')
        else:
            print form.username.errors
            return HttpResponse('Error')

    return render(request, "registration/login.html")