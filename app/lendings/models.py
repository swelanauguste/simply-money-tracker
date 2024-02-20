from decimal import Decimal

from django.db import models
from django.db.models import Sum


class LendingType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Lending(models.Model):
    lending_type = models.ForeignKey(LendingType, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_balance = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @classmethod
    def get_sum_of_lendings(cls):
        total_start_balance = (
            cls.objects.aggregate(Sum("start_balance"))["start_balance__sum"] or 0
        )
        total_balance = cls.objects.aggregate(Sum("balance"))["balance__sum"] or 0
        total_sum = total_start_balance + total_balance
        return Decimal(total_sum).quantize(Decimal("0.00"))

    def __str__(self):
        return f"{self.name} (-${self.balance})"
