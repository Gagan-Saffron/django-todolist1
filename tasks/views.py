from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Task,DoneTask

from .forms import AddTaskForm
# Create your views here.

def home_view(request):
    my_form=AddTaskForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form=AddTaskForm()
    context={'tasks':Task.objects.all(), 'done':DoneTask.objects.all(), 'form':my_form}
    return render(request,'homepage.html',context)

def delete_task_view(request,task_id):
    task=Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect('/')

def done_task_view(request,task_id):
    done_task=Task.objects.get(id=task_id)
    obj=DoneTask.objects.create(task=done_task.task)
    done_task.delete()
    return HttpResponseRedirect('/')
    
def delete_done_view(request,task_id):
    task=DoneTask.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect('/')