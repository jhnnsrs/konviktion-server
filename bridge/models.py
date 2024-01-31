from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.conf import settings



class NotionIntegration(models.Model):
    """
    A dataset is a collection of data files and metadata files.
    It mimics the concept of a folder in a file system and is the top level
    object in the data model.

    """

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="omero_user",
        help_text="The user that created the dataset",
    )
    workspace = models.CharField(
        max_length=9000,
        help_text="The workspace",
        default="",
    )

    notion_token = models.CharField(
        max_length=9000,
        help_text="The notion token",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "workspace"],
                name="Unique user and workspace",
            )
        ]

    


