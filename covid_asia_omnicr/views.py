from django.shortcuts import render
import rest_framework as rf
from rest_framework.views import APIView
from rest_framework.response import Response
from covid_asia_omnicr.services import utils
from covid_asia_omnicr.services import const
# Create your views here.

class Result(APIView):
    def get(self):
        source_dict = const.source
        data = utils.getdata(source_dict)
        return Response({"Data":data})

        


