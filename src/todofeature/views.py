from django.shortcuts import render

# from django import forms
from todofeature.models import Task
from todofeature.forms import TaskForm


# Create your views here.
def todo_list_view(request):
    return render(request, "todo_list.html")


def todo_add_view(request):
    form = TaskForm(request.POST or None)
    return render(request, "add_todo.html", {"form": form})
