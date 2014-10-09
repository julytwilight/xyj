# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from guys.views.accounts import RegisterView


urlpatterns = patterns('', 
    url(r'^whatsup/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^seeyou/$', 'guys.views.accounts.logout', name='logout'),
    url(r'^welcome/$', RegisterView.as_view(), name='register'),
)