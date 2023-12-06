from django.contrib import admin
from .models import CurrencyRate


class CurrencyEurAdmin(admin.ModelAdmin):
    list_display = ("code", "effective_date", "mid")


admin.site.register(CurrencyRate, CurrencyEurAdmin)
