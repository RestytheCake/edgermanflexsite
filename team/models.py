from django.contrib.auth.models import User
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.db import models

# Create your models here.


class FileUpload(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    file = models.FileField()

    def __str__(self):
        return str(self.user)


class NickUserManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('User need a username')
        if not password:
            raise ValueError('User need a password')
        user_obj = self.model(username=self.name(username))
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj


class NickUser(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    discord_member = models.BooleanField(default=False)
    supporter = models.BooleanField(default=False)
    special = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    confirm = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = NickUserManager()

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_discord_member(self):
        return self.discord_member

    @property
    def is_supporter(self):
        return self.supporter

    @property
    def is_special(self):
        return self.special

    @property
    def is_active(self):
        return self.active


class forum_test(models.Model):
    user = models.CharField(max_length=32, unique=False)
    message = models.CharField(max_length=255)

    def __str__(self):
        return str(f'{self.user} -> {self.message}')

