from django.shortcuts import render, redirect, get_object_or_404
from .models import Budget, Income
from .forms import BudgetForm, IncomeForm
from django.db import models
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm

@login_required
def dashboard(request):
    # Existing code for budget calculations
    total_budget = Budget.objects.filter(user=request.user).aggregate(total_budget=models.Sum('amount'))['total_budget'] or Decimal('0.0')
    total_expense = Budget.objects.filter(user=request.user).aggregate(total_expense=models.Sum('expense'))['total_expense'] or Decimal('0.0')
    remaining_budget = total_budget - total_expense
    
    

    # Calculate total income for the user
    total_income = Income.objects.filter(user=request.user).aggregate(total_income=models.Sum('amount'))['total_income'] or Decimal('0.0')

    # Income data for displaying income list
    income_data = Income.objects.filter(user=request.user)
    
    remaining_balance = total_income - total_budget
    
    budget_data = []
    for budget in Budget.objects.filter(user=request.user):
        expense = budget.expense
        remaining = budget.amount - expense
        budget_data.append({
            'budget': budget,
            'expense': expense,
            'remaining': remaining,
        })
        
    return render(request, 'tracker/dashboard.html', {
        'budget_data': budget_data,
        'total_budget': total_budget,
        'total_expense': total_expense,
        'remaining_budget': remaining_budget,
        'remaining_balance' : remaining_balance,
        'total_income': total_income,  # Include total income
        'income_data': income_data,  # Pass income data to template
    })


@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('dashboard')
    else:
        form = BudgetForm()
    return render(request, 'tracker/add_budget.html', {'form': form})

@login_required
def edit_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id, user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'tracker/edit_budget.html', {'form': form})

@login_required
def delete_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id, user=request.user)
    if request.method == 'POST':
        budget.delete()
        return redirect('dashboard')
    return render(request, 'tracker/delete_budget.html', {'budget': budget})


@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')  # Redirect to dashboard after saving
    else:
        form = IncomeForm()
    return render(request, 'tracker/add_income.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'tracker/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
