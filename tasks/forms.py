from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    task=forms.CharField(max_length=35,label='New Task',)
    class Meta:
        model=Task
        fields=['task',]