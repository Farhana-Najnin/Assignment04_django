from django.shortcuts import render
from task . models import Task
def showPage(request):
    item = Task.objects.all()
    return render(request,'home.html', {'item': item})