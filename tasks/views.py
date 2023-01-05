from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models.functions import Lower
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def home(request):
    return render(
        request,
        "tasks/home.html",
    )


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user.profile
            task.save()
            messages.success(request, "New task created.")
            return redirect("tasks:task-list")
    else:
        form = TaskForm()
    return render(request, "tasks/create.html", {"form": form})


@login_required
def list_task(request):
    """ Return all tasks for given user ordered by due_date, title, with null 'due date' tasks last """
    # TODO: Figure out what is used for ordering rows with `null` due date
    task_list = Task.objects.filter(author=request.user.profile.id).order_by(
        F("due_date").asc(nulls_last=True), Lower("title").asc()
    )

    context = {"tasks": task_list}

    return render(request, "tasks/list.html", context)
