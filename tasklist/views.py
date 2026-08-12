from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from datetime import date, timedelta


def tasklist(request):

    tasks = Task.objects.all()

    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    if start_date and end_date:
        tasks = tasks.filter(
            start_date__lte=end_date,
            end_date__gte=start_date,
        )

    elif start_date:
        tasks = tasks.filter(
            end_date__gte=start_date
        )

    elif end_date:
        tasks = tasks.filter(
            start_date__lte=end_date
        )

    context = {
        "tasks": tasks,
        "start_date": start_date,
        "end_date": end_date,
    }

    return render(request, "tasklist/task_list.html", context)


def task_create(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully!")
            return redirect("tasklist")

    else:
        form = TaskForm()

    return render(request, "tasklist/task_form.html", {"form": form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect("tasklist")

    return render(
        request,
        "tasklist/task_delete.html",
        {"task": task},
    )


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect("tasklist")

    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "tasklist/task_form.html",
        {
            "form": form,
            "task": task,
        },
    )

