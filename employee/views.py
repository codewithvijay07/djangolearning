from django.shortcuts import render,redirect
from employee.forms import EmployeeForm
from employee.models import Employee 
# Create your views here.
def emp(request):
    if(request.method=='POST'):
        form=EmployeeForm(request.POST)
        if(form.is_valid()):
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})

def show(request):
    employee=Employee.objects.all()
    return render(request,'display.html',{'employee':employee})

def remove(request,id):
    empl=Employee.objects.get(id=id)
    empl.delete()
    return redirect('/show')

def edit(request,id):
    empl=Employee.objects.get(id=id)
    return render(request,'update.html',{'empl':empl})

def update(request,id):
    empl=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=empl)
    if(form.is_valid()):
        form.save()
        return redirect('/show')
    return redirect(request,'update.html',{'empl':empl})

def index(request):
    return render(request,'home.html')