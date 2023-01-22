from django.contrib import admin

from projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'owner',
        'technology',
    ]
    # Excluding `image` from the admin form, so it renders properly in
    # Admin Interface. There may be some other way to resolve this issue.
    exclude = [
        'image'
    ]
