from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'expenditures/index.html')


def add_expenditure(request):
    return render(request, 'expenditures/add_expenditure.html')
