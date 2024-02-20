from decimal import Decimal

from django.db import models
from django.db.models import Sum


class EarningType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Earning(models.Model):
    earning_type = models.ForeignKey(EarningType, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["name"]

    @property
    def balance(self):
        total_expenses = self.expense_set.aggregate(Sum("amount"))["amount__sum"] or 0
        return Decimal(self.start_balance - total_expenses).quantize(Decimal("0.00"))

    def __str__(self):
        return f"{self.name} (${self.balance})"
