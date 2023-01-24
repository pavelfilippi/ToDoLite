from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from taggit.models import Tag
from .forms import TaskForm, TaskEditForm
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
            form.save_m2m()
            messages.success(request, "New task created.")
            return redirect("tasks:task-list")
    else:
        form = TaskForm()
    return render(request, "tasks/create.html", {"form": form})


@login_required
def list_task(request, tag_slug=None):
    """Return all tasks for given user ordered by due_date, title, with null 'due date' tasks last"""
    task_list = Task.objects.filter(author=request.user.profile.id).order_by(
        F("due_date").asc(nulls_last=True), Lower("title").asc()
    )
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        task_list = task_list.filter(tags__in=[tag])

    context = {"tasks": task_list}

    return render(request, "tasks/list.html", context)


@login_required
def edit_task(request, pk):
    """Edit task"""
    task = Task.objects.get(author=request.user.profile, pk=pk)
    if request.method == "POST":
        task_form = TaskEditForm(instance=task, data=request.POST)
        if task_form.is_valid():
            task_form.save()
            messages.success(request, "Task updated successfully")
            return redirect("tasks:task-list")
        else:
            messages.error(request, "Error updating your task")
    else:
        task_form = TaskEditForm(instance=task)

    return render(request, "tasks/edit.html", {"form": task_form})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, author=request.user.profile, pk=pk)

    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect(reverse("tasks:task-list"))

    return render(request, "tasks/delete.html", context={"task": task})
