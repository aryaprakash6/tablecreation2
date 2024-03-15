from django.db import models

# Create your models here.
class  Dept(models.Model):
    Dept_no = models.IntegerField(primary_key=True)
    D_name = models.CharField(max_length=100)
    Loc = models.CharField(max_length=100)
class Emp(models.Model):
    Emp_no= models.IntegerField(primary_key=True)
    E_name = models.CharField(max_length=100)
    Job = models.CharField(max_length=100)
    MGR = models.IntegerField()
    Hiredate= models.DateField()
    Sal = models.IntegerField()
    Comm = models.IntegerField()
    Dept_no = models.OneToOneField(Dept,on_delete=models.CASCADE)

class Salgrade(models.Model):
    Grade = models.IntegerField(primary_key=True)
    Losal = models.IntegerField()
    Hisal = models.IntegerField()

class Bonus(models.Model):
    E_name = models.CharField(max_length=100)
    Job = models.CharField(max_length=100)
    Sal = models.IntegerField()
    Comm = models.IntegerField()




