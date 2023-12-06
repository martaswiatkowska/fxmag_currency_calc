from .models import CurrencyRate
from .serializers import (
    CurrencyRateSerializer,
    CurrencyDataSerializer,
    CalculatedValueSerializer,
)
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, serializers, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import httpx
import pdb


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def post_list(request):
    request_serializer = CurrencyDataSerializer(data=request.query_params)

    if request_serializer.is_valid():
        currency = request.query_params.get("currency")

        queryset = (
            CurrencyRate.objects.filter(code=currency)
            .order_by("-effective_date")
            .last()
        )
        serializer = CurrencyRateSerializer(queryset)
        return Response(serializer.data)
    else:
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def calculated_value(request):
    request_serializer = CalculatedValueSerializer(data=request.query_params)

    if request_serializer.is_valid():
        value_from = float(request.query_params.get("value_from"))
        currency_from = request.query_params.get("in_currency")
        currency_to = request.query_params.get("out_currency")

        value_in = rate_for_currency(currency_from)
        value_out = rate_for_currency(currency_to)
        result = value_from * (value_in / value_out)

        return Response({"result": round(result, 4)})
    else:
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def rate_for_currency(currency):
    if currency == "PLN":
        return 1.0
    else:
        return (
            CurrencyRate.objects.filter(code=currency)
            .order_by("-effective_date")
            .last()
            .mid
        )
