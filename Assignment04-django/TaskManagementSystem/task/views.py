from django.shortcuts import render,redirect
from . import forms 
from . import models 
# Create your views here.
def addTask(request):
    if request.method == 'POST':
        taskItem = forms.TaskForm(request.POST)
        if taskItem.is_valid():
            taskItem.save()
            return redirect('addTask')
    else:
        taskItem = forms.TaskForm()
    return render(request,'add_task.html',{'form': taskItem})

def editTask(request,id):
    task = models.Task.objects.get(pk=id)
    taskItem = forms.TaskForm(instance=task)
    if request.method == 'POST':
        taskItem = forms.TaskForm(request.POST,instance=task)
        if taskItem.is_valid():
            taskItem.save()
            return redirect('showPage')
    return render(request,'add_task.html',{'form' : taskItem})

def deleteTask(request,id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('showPage')