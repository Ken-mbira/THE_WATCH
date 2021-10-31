from django.db import models

from mptt.models import MPTTModel,TreeForeignKey

# Create your models here.
class Location(MPTTModel):
    """A collection of all locations

    Args:
        MPTTModel ([type]): [description]
    """
    name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        verbose_name="Location",
        help_text="format:required, max_length=100",
        unique=True,
    )

    parent = TreeForeignKey("self",
    on_delete=models.PROTECT,
    related_name="children",
    null=True,
    unique=False,
    blank=True,
    verbose_name="parent of location",
    help_text="Format: not required"
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
