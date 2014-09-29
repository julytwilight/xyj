from django.contrib import admin
from .models import Production


class ProductionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'num')


admin.site.register(Production, ProductionAdmin)