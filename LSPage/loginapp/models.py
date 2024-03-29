from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    

class CustomUser(AbstractUser):
     company_name = models.CharField(max_length=100)
     role = models.CharField(max_length=100)
    # username= models.CharField(max_length=100,unique=True)

     groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_groups')
     user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions')
    #  EMAIL_FIELD = 'email'

     username = None
     email = models.EmailField(_('Email address'), unique=True,blank=True)
     
     required=True
     
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = []

     objects = CustomUserManager()


     def __str__(self):
        # return self.username
         return self.email
