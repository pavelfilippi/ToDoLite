from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "get_author_username"]
    list_filter = (("author", admin.RelatedOnlyFieldListFilter),)
    search_fields = ["title", "author__user__username"]
    readonly_fields = ["created_at", "updated_at"]

    @admin.display(description="Author", ordering="user__username")
    def get_author_username(self, obj):
        return obj.author.user.username
