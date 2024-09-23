from django import forms
from employee.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Employee