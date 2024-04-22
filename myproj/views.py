from django.shortcuts import render
from emp.models import Emp

def home(request):
    employees = Emp.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'home.html', context)