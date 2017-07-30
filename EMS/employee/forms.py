from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'surname', 'job_title', 'date_started', 'job_description', 'photo']

