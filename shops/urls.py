# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('', 
    url(r'yummy/$', 'shops.views.productions.index', name="productions-list"),
    url(r'yummy/detail/$', 'shops.views.productions.detail', name="productions-detail"),
)