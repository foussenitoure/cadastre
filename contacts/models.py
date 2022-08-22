from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.forms import forms
from django.contrib.gis.db import models as gis_models
import random
from random import randint
# from django.db.models.AutoField
# from django.contrib.auth.models import  User, AbstractUser
from django.db import models
from pyblog import settings
from django.db.models.signals import post_save


# ==============================================
#                  MODELE GISCONSULTING4
#                        START
# ==============================================



# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError("Vous devez entrer un addresse email.")
#         user = self.model(email=self.normalize_email(email))
#         user.set_password =(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password=None):
#        user = self.create_user(email=email, password=password)
#        user.is_admin = True
#        user.is_staff = True
#        user.save()
#        return user

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=8, blank=False)
    # email = models.EmailField(
    #     unique=True,
    #     max_length=255,
    #     blank=True,
    # )
    # name = models.CharField(max_length=50, blank=True)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)
    #
    # USERNAME_FIELD = "username"
    # objects = MyUserManager()
    #
    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     return True

class Profile(models.Model):
    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)



class Post(models.Model):
    id = models.AutoField(primary_key=True)
    DOMAINE    = (
        ('GEOMATIQUE', 'GEOMATIQUE'),
        ('BTP',        'BTP'),
        ('ARTISANAT', 'ARTISANAT'),)

    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )
    content    = models.TextField(verbose_name='Post')
    status     = models.IntegerField(choices=STATUS, default=0)
    slug       = models.SlugField(max_length=200, unique=True)
    title      = models.CharField(max_length=200, blank=True, verbose_name='Title')
    # author     = models.ForeignKey(User, on_delete= models.CASCADE,related_name='Blog_posts')
    domaine   = models.CharField(max_length=10, choices=DOMAINE, null=True, blank=True,)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    domicile   = models.CharField(max_length=100, null=True, blank=True, default='')
    image      = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Photo')
    # like        = models.IntegerField()
    # comment     = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}'.format(self.title)

# ==============================================
#                  MODELE GISCONSULTING4
#                        END
# ==============================================
