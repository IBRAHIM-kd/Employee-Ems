from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Employee
from .forms import EmployeeForm



def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employ/employee_list.html', {'employees': employees})


def save_employee_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            employee = Employee.objects.all()
            data['html_employee_list'] = render_to_string('employ/includes/employee_list.html', {
                'employee': employee
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
    else:
        form = EmployeeForm()
    return save_employee_form(request, form, 'employ/includes/employee_create.html')


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
    else:
        form = EmployeeForm(instance=employee)
    return save_employee_form(request, form, 'employ/includes/employee_update.html')


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    data = dict()
    if request.method == 'POST':
        employee.delete()
        data['form_is_valid'] = True
        employees = Employee.objects.all()
        data['html_employee_list'] = render_to_string('employ/includes/employee_list.html', {
            'employees': employees
        })
    else:
        context = {'employee': employee}
        data['html_form'] = render_to_string('employ/includes/employee_delete.html', context, request=request)
    return JsonResponse(data)
