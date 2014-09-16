# -*- coding: utf-8 -*-
from ahead.utils.lazy import *


def index(request):
    return render(request, "productions/index.html", {})