from django.urls import path

from .views import post_list, calculated_value

urlpatterns = [
    path("calculator/", post_list, name="currency_data"),
    path("calculated_value/", calculated_value, name="calculated_value"),
]
