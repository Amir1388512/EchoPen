from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.timezone import now
from .managers import *
from django.urls import reverse
from django.utils.text import slugify


# My User Model
class User(AbstractBaseUser):
    # Fields
    Username = models.CharField(max_length=10, unique=True)
    Email = models.EmailField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    DateOfJoined = models.DateTimeField(default=now)

    slug = models.SlugField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = "Username"
    REQUIRED_FIELDS = ["Email"]

    # Some Methods
    def __str__(self):
        return self.Username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_absolute_url(self):
        return reverse('Dashboard', args=self.slug)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.Username)
        super().save(*args, **kwargs)


# Article Model

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    created_time = models.DateTimeField(default=now)
    STATUS_CHOICES = (
        ("Pending", "PEN"),
        ("Rejected", "REJ"),
        ("Published", "PUB"),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="Pending")
    title = models.CharField(max_length=40, unique=True)
    like = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    objects = models.Manager()

    published = PublishedManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Article', kwargs={'slug': self.slug})
