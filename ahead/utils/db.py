# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DateTimeModel(models.Model):
    create_at = models.DateTimeField(_('date created'), auto_now_add=True)
    update_at = models.DateTimeField(_('date updated'), auto_now=True)
    
    class Meta:
        abstract = True