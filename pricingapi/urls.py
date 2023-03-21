from django.urls import path
from pricingapi import (
    views
)

urlpatterns = [
    path('calc_fare/', views.CalculateFare.as_view())
]
