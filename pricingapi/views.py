from django.shortcuts import render
from decimal import Decimal
from rest_framework.response import Response
from rest_framework.views import APIView
from pricingapi.models import *

class CalculateFare(APIView):
    def post(self, request):
        start_time = request.data["start_time"]
        end_time = request.data["end_time"]
        start_km = request.data["start_km"]
        end_km = request.data["end_km"]
        user_id = request.data["user_id"]
        driver_id = request.data["driver_id"]
        distance = end_km - start_km
        time_taken = end_time - start_time
        
        dbp = DecimalBasePrice.objects.filter(enable=True).first()
        if not dbp:
            return Response("No value is enabled for DBP")
        
        dap = DistanceAdditionalPrice.objects.filter(enable=True).first()
        if not dap:
            return Response("No value is enabled for DAP")
        
        tmf = TimeMultiplierFactor.objects.filter(time__gte=time_taken).first()
        if not tmf:
            return Response("No value is enabled for TMF")
        
        dap_value = dap.price / dap.distance
        additional_distance = Decimal(distance) - dbp.distance

        price = (dbp.price + (additional_distance * dap_value)) * tmf.multiple_factor
        driver_obj = Driver.objects.filter(pk=driver_id).first()
        user_obj = User.objects.filter(pk=user_id).first()
        ride = Ride(price=price, start_time=start_time, 
                    end_time=end_time, distance = distance,
                    driver = driver_obj, user = user_obj, 
                    vechile_id = driver_obj.vechile_id, dbp = dbp, dap = dap, tmf = tmf)
        
        ride.save()
        return Response(f"Calculated fare is {price}")