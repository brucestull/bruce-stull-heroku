from django.contrib import admin

from blog.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'date_posted',
        'display_categories',
    )
    list_filter = (
        'date_posted',
        'author',
        'categories',
    )
    search_fields = (
        'title',
        'body',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_created',
    )
    list_filter = (
        'name',
        'date_created',
    )
  