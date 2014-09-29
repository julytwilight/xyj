# -*- coding: utf-8 -*-
from ahead.utils.lazy import *
from ..models import Production


def index(request):
    productions = Production.objects.filter(state=1)
    return render(request, "productions/index.html", {'productions': productions})


def detail(request):
    return render(request, "productions/yummy.html")