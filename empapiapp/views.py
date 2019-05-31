from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from.models import Emp
def Emplist(request):
    data=Emp.objects.all()
    s={"results":list(data.values('ename','esal','email'))}
    return JsonResponse(s)