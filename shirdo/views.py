from django.shortcuts import render, redirect
from .forms import DoForm
from .models import Do
from django.contrib import  messages

def home(request):
    if request.method == "POST":
        form = DoForm(request.POST or None)
        if form.is_valid():
            form.save()
            tasks = Do.objects.all()
            messages.success(request, ("Item hass been added to the list"))
            return render(request, "home.html", {"tasks": tasks})
    else:
        tasks = Do.objects.all()
    return render(request, "home.html", {"tasks": tasks})
    
def delete(request, task_id):
    task = Do.objects.get(id=task_id)
    task.delete()
    messages.warning(request, ("your task has been deleted"))
    return redirect("home")


def cross_off(request, task_id):
    task = Do.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect("home")


def uncross(request, task_id):
    task = Do.objects.get(id=task_id)
    task.completed = False
    task.save()
    return redirect("home")


def update(request, task_id):
    if request.method == "POST":
        task = Do.objects.get(id=task_id)

        form = DoForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,"you have updated your task successfuly")
            return redirect("home")
    else:
        task = Do.objects.get(id=task_id)
        return render(request, "edit.html", {"task": task})
        
