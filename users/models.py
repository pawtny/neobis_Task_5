import jwt

from datetime import datetime, timedelta

from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models

class Role(models.Model):
    name = models.CharField("name of the role", max_length = 25, unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Roles"

class UserManager(BaseUserManager):
    def create_user(self, name, surname, username, email, roleid, phone, password=None):
        if name is None:
            raise TypeError('Users must have a name.')

        if surname is None:
            raise TypeError('Users must have a surname.')

        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        if phone is None:
        	raise TypeError('Users must have a phone number')

        user = self.model(name=name, surname = surname, username=username, email=self.normalize_email(email), roleid=roleid, phone=phone)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, name, surname, username, email, roleid, phone, password):
        admin_role = Role.objects.get(pk=roleid)
        if username is None:
            raise TypeError('Superusers must have a username.')
        
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(name=name,
                            surname = surname,
                            username=username,
                            email=self.normalize_email(email),
                            roleid=admin_role,
                            phone=phone,
                            password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField("name of the user", max_length = 30)
    surname = models.CharField("surname of the user", max_length = 30)
    username = models.CharField("username of the user", db_index=True, max_length=30, unique=True)
    email = models.EmailField("email of the user", unique=True)
    roleid = models.ForeignKey(Role, null = True, on_delete = models.SET_NULL)
    phone = models.CharField("phone number of the user", max_length = 10)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    dateofadd = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'surname', 'email', 'roleid', 'phone']

    objects = UserManager()
