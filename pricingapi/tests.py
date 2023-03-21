from unittest import TestCase, mock
from django.http import HttpRequest
from decimal import Decimal
from pricingapi.views import CalculateFare
from pricingapi.models import (
    DecimalBasePrice,
    DistanceAdditionalPrice,
    TimeMultiplierFactor
)

class TestCalculateFare(TestCase):

    @mock.patch('pricingapi.views.TimeMultiplierFactor')
    @mock.patch('pricingapi.views.DistanceAdditionalPrice')
    @mock.patch('pricingapi.views.DecimalBasePrice')
    def test_get(self, mock_dbp, mock_dap, mock_tmf):
        dbp_obj = DecimalBasePrice()
        dbp_obj.price = 80
        dbp_obj.distance = Decimal(3)
        dbp_obj.id = 1
        
        dap_obj = DistanceAdditionalPrice()
        dap_obj.price = 30
        dap_obj.distance = Decimal(1)
        dap_obj.id = 1

        tmf_obj = TimeMultiplierFactor()
        tmf_obj.time = 2
        tmf_obj.multiple_factor = Decimal(1.25)
        tmf_obj.id = 1

        calc_fare_obj = CalculateFare()
        mock_dbp.objects.filter.return_value = mock.MagicMock(**{"first.return_value": None})
        req = HttpRequest()
        req.data = {"distance": 10}
        res = calc_fare_obj.get(request=req)
        self.assertEqual(res.data, "No value is enabled for DBP")

        mock_dbp.objects.filter.return_value = mock.MagicMock(**{"first.return_value": dbp_obj})
        mock_dap.objects.filter.return_value = mock.MagicMock(**{"first.return_value": None})
        res = calc_fare_obj.get(request=req)
        self.assertEqual(res.data, "No value is enabled for DAP")

        mock_dap.objects.filter.return_value = mock.MagicMock(**{"first.return_value": dap_obj})
        mock_tmf.objects.filter.return_value = mock.MagicMock(**{"first.return_value": None})
        res = calc_fare_obj.get(request=req)
        self.assertEqual(res.data, "No value is enabled for TMF")

        mock_tmf.objects.filter.return_value = mock.MagicMock(**{"first.return_value": tmf_obj})
        res = calc_fare_obj.get(request=req)
        self.assertEqual(res.data, "Calculated fare is 362.50")
