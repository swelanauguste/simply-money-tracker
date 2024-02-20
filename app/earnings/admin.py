from django.contrib import admin

from .models import Earning, EarningType

admin.site.register(Earning)
admin.site.register(EarningType)
