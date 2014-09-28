# -*- coding: utf-8 -*-
from django.db import models

from ahead.utils.db import DateTimeModel
# Create your models here.


class Production(DateTimeModel):
    STATE_CHOICES = (
        (0, '隐藏'),
        (1, '显示'),
        (2, '告罄'),
        (7, '热卖'),
    )

    name         = models.CharField("产品名称", max_length=60, unique=True)
    price        = models.DecimalField("价格", max_digits=5, decimal_places=2)
    ingredients  = models.CharField("原料", max_length=255, blank=True)
    guarantee    = models.PositiveSmallIntegerField("保质期", default=6)
    introduction = models.TextField("介绍", blank=True)
    pic1         = models.ImageField("图片1", upload_to="productions")
    pic2         = models.ImageField("图片2", upload_to="productions")
    weight       = models.PositiveSmallIntegerField("重量", default=0)
    origin       = models.CharField("产地", max_length=30, blank=True)
    state        = models.PositiveSmallIntegerField("状态", choices=STATE_CHOICES, default=1)