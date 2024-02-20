from django.db import models
from earnings.models import Earning
from lendings.models import Lending


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    from_account = models.ForeignKey(Earning, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.category} - {self.amount}"


class IncomeCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    to_account = models.ForeignKey(Earning, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.category} - {self.amount}"


class Transfer(models.Model):
    from_account = models.ForeignKey(
        Earning, on_delete=models.CASCADE, related_name="transfer_from_account"
    )
    to_account = models.ForeignKey(
        Earning, on_delete=models.CASCADE, related_name="transfer_to_account"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.from_account} - {self.to_account} - {self.amount}"
