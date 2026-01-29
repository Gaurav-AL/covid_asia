from django.contrib import admin
from django.urls import path,include
from covid_asia_omnicr.views import Result, home


urlpatterns = [
    path('', home, name='home'),
    path('cases',Result.as_view()),
]