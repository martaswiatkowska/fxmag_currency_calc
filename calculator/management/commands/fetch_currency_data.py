from django.core.management.base import BaseCommand, CommandError
from calculator.models import CurrencyRate
from django.conf import settings
from datetime import date
from rest_framework import status
import httpx
from dateutil import parser


class Command(BaseCommand):
    help = "Fetch currency data"

    def add_arguments(self, parser):
        parser.add_argument("--effective_date", nargs="+")

    def handle(self, *args, **options):
        CURRENCIES = ["USD", "EUR"]

        effective_date_args = (
            parser.parse(options["effective_date"][0])
            if options["effective_date"]
            else ""
        )
        effective_date = (effective_date_args or date.today()).strftime("%Y-%m-%d")

        for code in CURRENCIES:
            self.fetch_data_for(code, effective_date)

        self.stdout.write("End of command")

    def fetch_data_for(self, currency, effective_date):
        r = httpx.get(
            "http://api.nbp.pl/api/exchangerates/rates/A/"
            + currency
            + "/"
            + effective_date
            + "/"
        )

        if r.status_code == status.HTTP_404_NOT_FOUND:
            raise CommandError("There is no rate for that date")
        else:
            data = r.json()
            rate = CurrencyRate.objects.filter(
                effective_date=effective_date, code=currency
            ).first()
            if rate == None:
                new_rate = CurrencyRate(
                    code=data["code"],
                    mid=data["rates"][0]["mid"],
                    effective_date=data["rates"][0]["effectiveDate"],
                )
                new_rate.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        'Successfully fetched data for curency %s : "%s"'
                        % (currency, new_rate)
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        "Rate for %s from day %s already imported"
                        % (currency, effective_date)
                    )
                )
