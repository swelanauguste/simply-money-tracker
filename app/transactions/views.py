from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from earnings.models import Earning
from lendings.models import Lending

from .forms import ExpenseForm, IncomeForm
from .models import Expense, Income


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    success_url = reverse_lazy("/")  # Replace with the actual URL name

    def form_valid(self, form):
        form.instance.from_account = form.cleaned_data["from_account"]
        return super().form_valid(form)


class DashboardView(TemplateView):
    lendings = Lending.objects.all()
    earnings = Earning.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lendings"] = Lending.objects.all()
        context["earnings"] = Earning.objects.all()
        return context

    template_name = "dashboard.html"


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    success_url = "/"


class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.to_account.balance += form.cleaned_data["amount"]
        form.instance.to_account.save()
        return super().form_valid(form)
