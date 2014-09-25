from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Production(models.Model):
    name = models.CharField(_('production name'), max_length=60, unique=True)
    