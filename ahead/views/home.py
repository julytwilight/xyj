# -*- coding: utf-8 -*-
from ahead.utils.lazy import *

def default(request):
    return render(request, "index.html", {})


def register(request):
    return render(request, "registration/login.html")