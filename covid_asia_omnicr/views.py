from django.shortcuts import render
import rest_framework as rf
from rest_framework.views import APIView
from rest_framework.response import Response
from covid_asia_omnicr.services import utils
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.core.cache import cache
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'index.html')

class Result(APIView):
    @swagger_auto_schema(
        operation_description="Get latest COVID-19 data for Asian countries (cached for 30 seconds)",
        responses={200: openapi.Response('Success response', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'Data': openapi.Schema(type=openapi.TYPE_OBJECT, description='Country-wise data with cumulative, delta stats, and source URL'),
                'origin': openapi.Schema(type=openapi.TYPE_STRING, description='Data source: "cached" from cache or "fresh" from scraping')
            }
        ))}
    )
    def get(self, request):
        cache_key = 'covid_data'
        data = cache.get(cache_key)
        if data:
            origin = "cached"
        else:
            origin = "fresh"
            data = utils.updateDeltaStats_CumulativeStats()
            cache.set(cache_key, data, settings.CACHE_TIMEOUT)
        return Response({"Data": data, "origin": origin})

        


