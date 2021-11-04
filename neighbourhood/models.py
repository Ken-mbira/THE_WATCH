from django.db import models
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from mptt.models import MPTTModel,TreeForeignKey
from cloudinary.models import CloudinaryField

from account.models import Account

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

class Neighbourhood(models.Model):
    """This define the behaviors of a neighborhood

    Args:
        models ([type]): [description]
    """
    name = models.CharField(
        max_length=50,
        blank = False,
        null=False,
        verbose_name="neighbourhood name",
        help_text="format: required"
    )

    location = models.ForeignKey(
        Location,
        null=False,
        blank = False,
        related_name="neighbourhood",
        on_delete=models.PROTECT
    )

    slogan = models.CharField(
        max_length=50,
        blank = False,
        null=False,
        verbose_name="slogan",
        help_text="format: required, max_length=50"
    )

    police_hotline = models.CharField(
        max_length=10,
        blank = False,
        null=False,
        verbose_name="police hotline",
        help_text="format: required"
    )

    hospital_hotline = models.CharField(
        max_length=10,
        blank = False,
        null=False,
        verbose_name="hospital hotline",
        help_text="format: required"
    )

    admin = models.OneToOneField(
        Account,
        related_name="is_admin_in",
        on_delete=models.SET_NULL,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    image = CloudinaryField("images/",
        null=True,
    )

    def __str__(self):
        return self.name


class Profile(models.Model):
    """This extends the user model and provides an interface to connect to the neighbourhood class

    Args:
        models ([type]): [description]
    """
    user = models.OneToOneField(Account,null=False,related_name="profile",on_delete=models.CASCADE,)
    neighbourhood = models.ForeignKey(Neighbourhood,null=True,blank=True,on_delete=models.SET_NULL,related_name="user")

    def __str__(self):
        return self.user.username + "'s " + "profile"

    @receiver(post_save, sender=Account)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=Account)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
    """This defines a user business in a particular neighbourhood

    Args:
        models ([type]): [description]
    """

    owner = models.ForeignKey(
        Account,
        related_name="business",
        null=False,
        blank=False,
        verbose_name="owner of business",
        on_delete=models.CASCADE,
        help_text="owner of business"
    )

    name = models.CharField(
        max_length=50,
        blank = False,
        null=False,
        verbose_name="business name",
        help_text="format: required",
        unique=True
    )

    services = models.ForeignKey(
        Services,
        related_name="business",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="services offered",
    )

    image = CloudinaryField(
        'images/',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name + " | " + self.owner.username

    def get_bussinesses(pk):
        """This returns all businesses provided a neighbourhood

        Returns:
            [type]: [description]
        """
        neighbourhood = Neighbourhood.objects.get(pk=pk)
        
        bussinessOwners = Account.objects.filter(profile__neighbourhood = neighbourhood)

        businesses = []
        for i in bussinessOwners:
            try:
                business = Business.objects.get(owner = i)
                businesses.append(business)
            except:
                continue

        return businesses




class Occurrence(models.Model):
    """This defines an occurence to be reported by a user

    Args:
        models ([type]): [description]
    """
    type = models.ForeignKey(
        EventType,
        null=False,
        blank=False,
        related_name="occurred_events",
        on_delete=models.PROTECT
    )

    name = models.CharField(
        max_length=50,
        blank = False,
        null=False,
        verbose_name="ocurrence name",
        help_text="format: required"
    )

    description = models.TextField(
        blank = False,
        null=False,
        verbose_name="occurence description",
        help_text="format: required"
    )

    reporter = models.ForeignKey(
        Account,
        related_name="reported_events",
        on_delete=models.SET_NULL,
        null=True,
    )

    image_description = CloudinaryField(
        'images/',
        blank=False,
        null=False,
    )

    neighbourhood = models.ForeignKey(
        Neighbourhood,
        null=False,
        blank=False,
        related_name="reported_events",
        on_delete=models.CASCADE,
    )

    reported_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    to_happen_at = models.DateField(
        null=True,
        blank=True,
        verbose_name="scheduled time"
    )

    def __str__(self) -> str:
        return self.name + " by " + self.reporter.username