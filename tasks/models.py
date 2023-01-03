from django.db import models

from account.models import Profile


class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
