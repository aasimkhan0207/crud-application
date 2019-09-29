from django.shortcuts import render, redirect
from crudapp.forms import EmployeeForm
from crudapp.models import Employee

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid(): # if valid then save
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "index.html", {'form':form})

@login_required
def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees':employees})

@user_passes_test(lambda u: u.is_superuser)
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee':employee})

@user_passes_test(lambda u: u.is_superuser)
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit.html", {'employee':employee})

@user_passes_test(lambda u: u.is_superuser)
def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
