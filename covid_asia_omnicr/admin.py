from django.contrib import admin

# Register your models here.
from covid_asia_omnicr.models import Countries
from covid_asia_omnicr.models import CumulativeStats
from covid_asia_omnicr.models import DeltaStats

admin.site.register(Countries)
admin.site.register(CumulativeStats)
admin.site.register(DeltaStats)
