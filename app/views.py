from django.shortcuts import render

# Create your views here.
from app.models import *

def display_dept(request):
    QLDO = Dept.objects.all()
    d={'dept':QLDO}
    return render(request, 'display_dept.html', d)



def display_emp(request):
    QLEO = Emp.objects.all()
    d={'emp': QLEO}
    return render(request, 'display_emp.html', d)




def insert_dept(request):
    dno=int(input('enter dept no'))
    dname=input('enter name')
    l=input('enter loc')
    NDO = Dept.objects.get_or_create(Dept_no=dno, D_name=dname, Loc=l)[0]
    NDO.save()
    QLDO = Dept.objects.all()
    d={'dept':QLDO}
    return render(request, 'display_dept.html', d)

def insert_emp(request):
    eno=int(input('enter eno'))
    ename=input('enter name')
    j=input('enter job')
    mgr = input('enter mgr')
    h = input('enter hiredate')
    s=int(input('enter sal'))
    c=int(input('enter comm'))
    dno=int(input('enter dno'))
    NEO = Emp.objects.get_or_create(Emp_no=eno, E_name=ename, Job=j, MGR=mgr, Hiredate=h, Sal=s, Comm=c, Dept_no=dno)[0]
    NEO.save()
    QLEO = Emp.objects.all()
    d={'emp': QLEO}
    return render(request, 'display_emp.html', d)
    
