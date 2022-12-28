from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from todofeature.models import Task
from todofeature.forms import TaskForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def todo_list_view(request):
    tasks = Task.objects.all().order_by("priority")
    context = {"tasks": tasks}
    return render(request, "todo_list.html", context)


def todo_add_view(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect(reverse("todofeature:todo_list"))
    return render(request, "add_todo.html", {"form": form})


def todo_edit_view(request, taskid):
    task = get_object_or_404(Task, id=taskid)

    # above code means
    # try:
    #     Task.objects.get(id=taskid)
    # except Task.DoesNotExist:
    #     return Http404()

    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("todofeature:todo_list"))
    return render(request, "add_todo.html", {"form": form})
