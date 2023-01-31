from django import forms
from django.utils import timezone
from taggit.forms import TagWidget

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "due_date", "tags"]
        widgets = {
            "due_date": forms.DateInput(attrs={"class": "datepicker", "type": "date"}),
            "tags": TagWidget(),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data["due_date"]
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError("The due date cannot be in the past.")
        return due_date


class TaskEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].required = False
        self.fields["due_date"].required = False
        self.fields["completed"].required = False
        self.fields["tags"].required = False

    class Meta:
        model = Task
        fields = ["title", "due_date", "completed", "tags"]
        widgets = {
            "due_date": forms.DateInput(attrs={"class": "datepicker", "type": "date"}),
            "tags": TagWidget(),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data["due_date"]
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError("The due date cannot be in the past.")
        return due_date


class SearchForm(forms.Form):
    query = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"placeholder": "Type your search query here:"}), label=""
    )
