from django.contrib import admin
from .models import Budget, Income

# Register the Budget model
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount', 'expense', 'remaining', 'created_at', 'user')  # Customize list view
    search_fields = ('name', 'category', 'user__username')  # Enable search by name, category, and user
    list_filter = ('category', 'user')  # Enable filtering by category and user

admin.site.register(Budget, BudgetAdmin)

# Register the Income model
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('source', 'amount', 'created_at', 'user')  # Customize list view
    search_fields = ('source', 'user__username')  # Enable search by source and user
    list_filter = ('user',)  # Enable filtering by user

admin.site.register(Income, IncomeAdmin)
