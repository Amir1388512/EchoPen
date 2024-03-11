from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.timezone import now
from .managers import UserManager
from django.urls import reverse
from django.utils.text import slugify


# My User Model
class User(AbstractBaseUser):
    # Fields
    Username = models.CharField(max_length=15, unique=True)
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
        return self.Email

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