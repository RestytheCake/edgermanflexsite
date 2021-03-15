from django.contrib.auth.models import User
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.db import models
from django.conf import settings
# Create your models here.


class FileUpload(models.Model):

    user = models.CharField(max_length=255, blank=True, default=',')
    file = models.FileField()

    def __str__(self):
        return str(self.user)


class NickUserManager(BaseUserManager):

    def create_user(self, username, password, is_staff=False, is_admin=False):
        if not username:
            raise ValueError('User need a username')
        if not password:
            raise ValueError('User need a password')
        user_obj = self.model(username=username)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, password):
        if not username:
            raise ValueError('User need a username')
        if not password:
            raise ValueError('User need a password')
        user = self.create_user(
            username=username,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class NickUser(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    discord_member = models.BooleanField(default=False)
    discord_name = models.CharField(max_length=255, unique=False, blank=True)
    supporter = models.BooleanField(default=False)
    special = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    confirm = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = NickUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

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
    def is_discord_name(self):
        return self.discord_name

    @property
    def is_supporter(self):
        return self.supporter

    @property
    def is_special(self):
        return self.special

    @property
    def is_active(self):
        return self.active


class forum(models.Model):
    user = models.CharField(max_length=255, default=' ')
    title = models.CharField(max_length=100, unique=False, blank=False, default='')
    message = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f'{self.user} -> {self.title} : {self.message}')


class profile(models.Model):
    username = models.CharField(max_length=255, blank=True, unique=True)
    discord_member = models.BooleanField(default=False)
    discord_name = models.CharField(max_length=255, blank=True)
    special = models.BooleanField(default=False)
    special_roles = models.CharField(max_length=255, blank=True)
    long_supporter = models.BooleanField(default=False)
    muffin_family = models.BooleanField(default=False)
    muffin_role = models.CharField(max_length=255, blank=True)

    def __str__(self):
        if self.discord_member:
            if self.muffin_family:
                if self.special_roles:
                    return str(f'{self.username} -> {self.discord_name} -> {self.muffin_role} -> {self.special_roles}')
                else:
                    return str(f'{self.username} -> {self.discord_name} -> {self.muffin_role}')
            else:
                if self.special_roles:
                    return str(f'{self.username} -> {self.discord_name} -> {self.special_roles}')
                else:
                    return str(f'{self.username} -> {self.discord_name}')
        else:
            if self.special:
                return str(f'{self.username} -> {self.special_roles}')
            else:
                return str(f'{self.username}')


class comment(models.Model):
    Username = models.CharField(max_length=255, blank=True, unique=False)
    main_post_user = models.CharField(max_length=255, blank=True, unique=False)
    main_post_title = models.CharField(max_length=255, blank=True, unique=False)
    comments = models.CharField(max_length=255, blank=False, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f'{self.Username} -> {self.main_post_user} -> {self.main_post_title} -> {self.comments}')

