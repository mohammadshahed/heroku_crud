from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import EmployeeForm
from .models import Employee


# Create your views here.

def employee_list(request):
	employee = Employee.objects.all()

	paginator = Paginator(employee, 3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

    
	context = {
    'employee_list':page_obj
	}
	return render(request, "employee_register/employee_list.html", context)




def employee_form(request, id=0):
	if request.method =='GET':
		if id == 0:
			form = EmployeeForm()
		else:
			employee = Employee.objects.get(pk=id)
			form = EmployeeForm(instance=employee)
		return render(request, "employee_register/employee_form.html", {'form':form})

	else:
		if id == 0:
			form = EmployeeForm(request.POST)
		else:
			employee = Employee.objects.get(pk=id)
			form = EmployeeForm(request.POST, instance=employee)		
		if form.is_valid():
			form.save()
		return redirect('/employee/list')	



def employee_delete(request, id):
	employee = Employee.objects.get(pk=id)
	employee.delete()

	return redirect('/employee/list') 	

