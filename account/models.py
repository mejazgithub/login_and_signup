from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if email==None:
            raise TypeError("User should have a email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password):
        if password is None:
            raise TypeError("User must have a password")
        user = self.create_user(email,password=password)
        user.save()

        user.is_superuser   = True
        user.is_staff       = True
        user.is_verified    = True
        user.is_approved    = True
        user.save()
        return user


class User(AbstractBaseUser,PermissionsMixin):

    first_name          = models.CharField(max_length=100, null=True,blank=True)
    last_name           = models.CharField(max_length=100, null=True,blank=True)
    email               = models.EmailField(max_length=50, unique=True, db_index=True)
    profile_picture     = models.ImageField(upload_to="profile_pictures/", default="profile_pictures/avatar_blank.jpg")
    is_approved         = models.BooleanField(default=False)
    is_verified         = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_owner            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


    USERNAME_FIELD  = 'email'
    objects = UserManager()
    def __str__(self):
        return "%s"%(self.email)
