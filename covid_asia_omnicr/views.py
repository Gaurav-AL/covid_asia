from django.shortcuts import render
import rest_framework as rf
from rest_framework.views import APIView
from rest_framework.response import Response
from covid_asia_omnicr.services import utils

# Create your views here.

class Result(APIView):
    def get(self,request):
        data = utils.updateDeltaStats_CumulativeStats()
        return Response({"Data":data})

        


