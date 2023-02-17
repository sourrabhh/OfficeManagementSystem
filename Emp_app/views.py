from django.shortcuts import render,HttpResponse
from .models import employee,role,department
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')


def view_emp(request):
    emps = employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'view_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = int(request.POST['salary'])
        role = request.POST['role']
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']
        
        new_emp = employee(first_name = first_name, last_name=last_name, dept_id = dept, salary = salary, role_id=role, phone = phone, hire_date=datetime.now() )
        new_emp.save()
        return HttpResponse('Employee Details Added Successfully !')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    # else:
    #     return HttpResponse("Exception Occured ")
    

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_remove = employee.objects.get(id = emp_id)
            emp_to_remove.delete()
            return HttpResponse("Record Deleted Successfully")
        except:
            return HttpResponse('Select Valid ID ')
    emps = employee.objects.all()
    context = {
        'emps' : emps
    }
    
    return render(request, 'remove_emp.html',context)

def del_emp(request):
    return render(request, 'del_emp.html')