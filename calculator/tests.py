from django.test import RequestFactory, TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from calculator.models import CurrencyRate
import urllib.request
from django.test import Client
from django.urls import reverse
from datetime import date
from .views import post_list, calculated_value

# Create your tests here.


class SimpleTests(APITestCase):
    def setUp(self):
        CurrencyRate(
            code="PLN",
            mid="1.0",
            currency="Polish zloty",
            effective_date=date(2023, 11, 11),
        ).save()
        CurrencyRate(
            code="EUR", mid="4.5", currency="Euro", effective_date=date(2023, 11, 11)
        ).save()
        CurrencyRate(
            code="USD", mid="6", currency="USD", effective_date=date(2023, 11, 11)
        ).save()

    def test_post_list(self):
        params = {"currency": "EUR"}
        response = self.client.get(reverse("currency_data"), params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list_return_data(self):
        params = {"currency": "EUR"}
        response = self.client.get(reverse("currency_data"), params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["effective_date"], "2023-11-11")
        self.assertEqual(response.data["mid"], 4.5)
        self.assertEqual(response.data["code"], "EUR")

    def test_post_list_empty_value(self):
        params = {"currency": ""}
        response = self.client.get(reverse("currency_data"), params)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_calculated_value(self):
        params = {"value_from": "10", "in_currency": "USD", "out_currency": "EUR"}
        response = self.client.get(reverse("calculated_value"), params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_calculated_value_return_proper_data(self):
        params = {"value_from": 10, "in_currency": "EUR", "out_currency": "PLN"}
        response = self.client.get(reverse("calculated_value"), params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["result"], 45.0)

    def test_calculated_value_emp(self):
        params = {"value_from": "123", "in_currency": "EUR", "out_currency": "PLN"}
        response = self.client.get(reverse("calculated_value"), params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_calculated_value_error(self):
        params = {"value_from": "123", "in_currency": "aaaa", "out_currency": "PLN"}
        response = self.client.get(reverse("calculated_value"), params)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_calculated_value_error_with_negative_value(self):
        params = {"value_from": -122, "in_currency": "PLN", "out_currency": "PLN"}
        response = self.client.get(reverse("calculated_value"), params)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
