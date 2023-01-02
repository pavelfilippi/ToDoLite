from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect

from .forms import TaskForm


def home(request):
    return render(
        request,
        "tasks/home.html",
    )


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user.profile
            task.save()
            messages.success(request, "New task created.")
            # TODO: Don't redirect to home, but to list when ready
            return HttpResponseRedirect(request.path_info)
    else:
        form = TaskForm()
    return render(request, "tasks/create.html", {"form": form})
