from django.db import models

from config.settings.common import AUTH_USER_MODEL


class Category(models.Model):
    """
    Model for blog `Post` `Catagory`s.
    """
    name = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model for blog `Post`s.
    """
    title = models.CharField(
        max_length=100,
    )
    body = models.TextField()
    date_posted = models.DateTimeField(
        auto_now_add=True,
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    categories = models.ManyToManyField(
        Category,
        related_name='posts',
        blank=True,
    )

    def __str__(self):
        return self.title

    def display_categories(self):
        """
        Returns a comma-separated list of `Category` names.
        """
        return ', '.join([category.name for category in self.categories.all()[:4]])

    display_categories.short_description = 'Categories'

class Comment(models.Model):
    """
    Model for blog `Post` `Comment`s.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    date_posted = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.body[:20]
