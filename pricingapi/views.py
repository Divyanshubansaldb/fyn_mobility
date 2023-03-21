from django.shortcuts import render
from decimal import Decimal
from rest_framework.response import Response
from rest_framework.views import APIView
from pricingapi.models import (
    DecimalBasePrice, 
    DistanceAdditionalPrice, 
    TimeMultiplierFactor
)

class CalculateFare(APIView):
    def get(self, request):
        distance = request.data["distance"]
        dbp = DecimalBasePrice.objects.filter(enable=True).first()
        if not dbp:
            return Response("No value is enabled for DBP")
        
        dap = DistanceAdditionalPrice.objects.filter(enable=True).first()
        if not dap:
            return Response("No value is enabled for DAP")
        
        tmf = TimeMultiplierFactor.objects.filter(enable=True).first()
        if not tmf:
            return Response("No value is enabled for TMF")

        dap_value = dap.price / dap.distance
        additional_distance = Decimal(distance) - dbp.distance

        price = (dbp.price + (additional_distance * dap_value)) * tmf.multiple_factor
        return Response(f"Calculated fare is {price}")