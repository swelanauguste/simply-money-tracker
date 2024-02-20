from django.urls import path

from .views import DashboardView, ExpenseCreateView, IncomeCreateView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("add-expense/", ExpenseCreateView.as_view(), name="expense-create"),
    path("add-income/", IncomeCreateView.as_view(), name="income-create"),
]
