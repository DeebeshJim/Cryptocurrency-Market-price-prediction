from django.contrib import admin

from .models import BitcoinPrediction, LitecoinPrediction, StellarPrediction
admin.site.register(BitcoinPrediction)
admin.site.register(LitecoinPrediction)
admin.site.register(StellarPrediction)