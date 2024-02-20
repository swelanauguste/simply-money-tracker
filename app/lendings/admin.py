from django.contrib import admin

from .models import Lending, LendingType

admin.site.register(Lending)
admin.site.register(LendingType)
