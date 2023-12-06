from .models import CurrencyRate
from rest_framework import serializers


class CurrencyRateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = ["effective_date", "mid", "code"]


class CurrencyDataSerializer(serializers.Serializer):
    currency = serializers.ChoiceField(choices=["PLN", "EUR", "USD"])


class CalculatedValueSerializer(serializers.Serializer):
    value_from = serializers.FloatField(min_value=0)
    in_currency = serializers.ChoiceField(choices=["PLN", "EUR", "USD"])
    out_currency = serializers.ChoiceField(choices=["PLN", "EUR", "USD"])
