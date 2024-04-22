from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from emp.models import Emp

# Create your views here.

def employee_detail(request, pk):
    employee = get_object_or_404(Emp, pk=pk)
    return HttpResponse(employee)
