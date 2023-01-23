from django.db import models

from config.settings.common import AUTH_USER_MODEL


class Project(models.Model):
    """
    Model for each project.

    An `owner` can have multiple `Project`s.
    """
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    technology = models.CharField(
        max_length=25,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image = models.FilePathField(
        "Image Location",
        path="/images",
    )

    def __str__(self):
        return self.title