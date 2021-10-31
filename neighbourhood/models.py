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


class EventType(models.Model):
    """This define the type of occurrence in the neighborhood

    Args:
        models ([type]): [description]
    """
    name = models.CharField(
        max_length=50,
        blank = False,
        null=False,
        verbose_name="event name",
        help_text="format: required"
    )

    description = models.TextField(
        blank = False,
        null=False,
        verbose_name="event description",
        help_text="format: required"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Event type"
        verbose_name_plural="Event types"


class Services(models.Model):
    """This defines the types of services offered in a business

    Args:
        models ([type]): [description]
    """
    name = models.CharField(
        max_length=50,
        blank = False,
        null=False,
        verbose_name="service name",
        help_text="format: required"
    )

    description = models.TextField(
        blank = False,
        null=False,
        verbose_name="service description",
        help_text="format: required"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Service type"
        verbose_name_plural="Service types"


