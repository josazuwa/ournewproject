from django.db import models
from datetime import datetime

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=400, default = "")
    def __str__(self):
        return self.name
class Faculty(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name
class Department(models.Model):
    name = models.CharField(max_length=80)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Certificate_Type(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name
class Grade(models.Model):
    classYear = models.CharField(max_length=1, default = "")
    def __str__(self):
        return str(self.classYear)
class Student(models.Model):
    fullname = models.CharField(max_length=80, default = "")
    year_of_graduation = models.IntegerField()
    department = models.ForeignKey(Department, default = "", on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, default = 0, on_delete=models.CASCADE)
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE, blank=True)
    certificate_type = models.ForeignKey(Certificate_Type, default = "", on_delete=models.CASCADE)
    def __str__(self):
        return self.fullname
