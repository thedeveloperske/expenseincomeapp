from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="expenditures"),
    path('add-expenditure', views.add_expenditure, name="add-expenditures"),
]
