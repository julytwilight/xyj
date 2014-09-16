# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('', 
    url(r'productions/$', 'shops.views.productions.index', name="production-list"),
)