from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('add-budget/', views.add_budget, name='add_budget'),
    path('edit-budget/<int:budget_id>/', views.edit_budget, name='edit_budget'),
    path('delete-budget/<int:budget_id>/', views.delete_budget, name='delete_budget'),
    path('add_income/', views.add_income, name='add_income'),
]
