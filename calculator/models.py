from django.db import models

# Create your models here.


class CurrencyRate(models.Model):
    effective_date = models.DateField("Effective date")
    mid = models.FloatField("converted average currency rate")
    code = models.CharField("Code of currency")
    currency = models.CharField("description")

    def __str__(self):
        return ", ".join(str(x) for x in [self.code, str(self.mid)])
