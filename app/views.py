from django.shortcuts import render

# Create your views here.
from app.models import *
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2500)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='DALLAS')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:]

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)


def selfjoins(request):
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename__contains='S')
    EMPOBJECTS=Emp.objects.select_related('mgr').all()
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(ename__startswith='A')
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(job='MANAGER')
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(job__endswith='k')
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(hiredate__month=1)
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(hiredate__month=1,deptno=20)
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename='SCOTT')
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=1500)
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(mgr__deptno=30)

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'selfjoins.html',d)


def emp_mgr_dept(request):
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').all()
    
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(ename='MARTIN')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(ename='ALLEN')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='JONES')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(ename='KING')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(ename='SCOTT')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(ename='JONES')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(ename='BLAKE')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(ename='CLARK')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__startswith='S')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__startswith='R')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__startswith='A')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__endswith='H')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__endswith='G')
    EMPOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__endswith='S')
    




    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'emp_mgr_dept.html',d)