# -*- coding: utf-8 -*-
from ahead.utils.lazy import *


def home(request):
    return render(request, "index.html", {})