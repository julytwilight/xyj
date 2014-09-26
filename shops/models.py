from django.db import models

from ahead.utils.db import DateTimeModel
# Create your models here.


class Production(models.Model, DateTimeModel):
    name         = models.CharField("产品名称", max_length=60, unique=True)
    price        = models.DecimalField("价格", max_digits=5, decimal_places=2)
    ingredients  = models.CharField("原料", max_length=255, blank=True)
    guarantee    = models.PositiveSmallIntegerField("保质期", default=6)
    introduction = models.TextField("介绍", blank=True)
    pic1         = models.ImageField(upload_to="productions")
    pic2         = models.ImageField()