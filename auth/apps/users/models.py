from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, first_name=""):
        user = self.model(username=username)
        user.first_name = first_name
        user.username = username
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None):
        user = self.create_user(password=password, username=username)
        user.is_staff = True
        user.is_superuser = True
        user.email = email
        user.save(using=self._db)

        return user


class Users(AbstractUser):
    NAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return self.username

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'is_superuser': self.is_superuser,
            'is_staff': self.is_staff,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    class Meta:
        db_table = 'users'
