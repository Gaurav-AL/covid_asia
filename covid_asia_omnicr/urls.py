from django.contrib import admin
from django.urls import path,include
from covid_asia_omnicr.views import Result


urlpatterns = [
    path('cases',Result.as_view()),
]