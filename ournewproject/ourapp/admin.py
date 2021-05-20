from django.contrib import admin
from django.db.models.expressions import F
from .models import School, Student, Faculty, Department, Certificate_Type, Grade

# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Certificate_Type)
admin.site.register(Grade)