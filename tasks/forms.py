from django import forms
from django.utils import timezone

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "due_date"]
        widgets = {
            "due_date": forms.DateInput(attrs={"class": "datepicker", "type": "date"}),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data["due_date"]
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError("The due date cannot be in the past.")
        return due_date
