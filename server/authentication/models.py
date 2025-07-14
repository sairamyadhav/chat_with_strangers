from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from .validators import validate_username, validate_password
from django.conf import settings

# Create your models here.

class AuthUserManager(BaseUserManager):
    def create_user(self, username=None, password=None, email=None, **kwargs):
        if not username:
            raise ValueError("The Username must be set")
        if not password:
            raise ValueError("The Password must be set")
        user = self.model(username=username, password=password, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username=None, password=None, email=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, email, **kwargs)

class AuthUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=64, blank=False, null=False, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AuthUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username