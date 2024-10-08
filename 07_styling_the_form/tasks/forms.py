# tasks/forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Title'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Task Due Date'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Task Category'}),
        }