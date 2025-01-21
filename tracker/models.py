from django.db import models
from django.contrib.auth.models import User

# Define choices for category
CATEGORY_CHOICES = [
    ('food', 'Food'),
    ('transport', 'Transport'),
    ('entertainment', 'Entertainment'),
    ('health', 'Health'),
    ('education', 'Education'),
    ('other', 'Other'),
]

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='other')  # Category with choices
    name = models.CharField(max_length=100)  # Name for the budget
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total budget amount
    expense = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Total expenses (this will be updated over time)
    remaining = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Remaining budget field
    created_at = models.DateTimeField(auto_now_add=True)  # Budget creation timestamp

    def __str__(self):
        return f"{self.name} ({self.category}): ${self.amount}"

    def save(self, *args, **kwargs):
        # Automatically update the remaining field when the budget or expense changes
        self.remaining = self.amount - self.expense
        super().save(*args, **kwargs)  # Call the parent save method


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount of income
    source = models.CharField(max_length=100)  # Source of income (e.g., salary, freelance)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when income was added

    def __str__(self):
        return f"Income from {self.source}: ৳{self.amount}"
