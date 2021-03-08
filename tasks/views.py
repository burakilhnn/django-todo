from django.shortcuts import render, redirect
from .models import Tasks
from datetime import date
from django import forms
from django.views.decorators.http import require_POST

today = date.today()

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

context = {'tasks':Tasks.objects.all(),'date':today.strftime("%B %d, %Y")}

def home(request):
    return render(request, 'tasks/home.html', context)

@require_POST
def add(request):
    if request.method == 'POST':
        data = request.POST['newItem']
        task = Tasks(task = data)
        task.save()
    return redirect('tasks:home')

@require_POST
def delete(request):
    if request.method == 'POST':
        data = request.POST['checkbox']
        Tasks.objects.filter(id=data).delete()
    return redirect('tasks:home')



