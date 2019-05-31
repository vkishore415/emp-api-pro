from django.contrib import admin
from.models import Emp
# Register your models here.
class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','esal','email']
    admin.site.register(Emp)