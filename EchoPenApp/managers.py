from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, Username, Email, password=None):
        if not Email:
            raise ValueError('Users must have an email address')

        user = self.model(
            Username=Username,
            Email=self.normalize_email(Email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Username, Email, password=None):
        user = self.create_user(
            Username=Username,
            Email=Email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user