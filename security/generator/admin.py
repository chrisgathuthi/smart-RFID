from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("reg_no","first_name","last_name","email","reg_date")
admin.site.register(Student,admin_class=StudentAdmin)