from django.db import models
from django.forms import forms
from django.contrib.gis.db import models as gis_models
import random
from random import randint
# from django.db.models.AutoField
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


from django.forms import widgets


# ==============================================
#                  MODELE GISCONSULTING4
#                        START
# ==============================================

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='posted', null=True, blank=True, verbose_name='Photo_commande')
    post = models.TextField(max_length=2000, blank=True, verbose_name=' post')
    title = models.CharField(max_length=30, blank=True, verbose_name='title')
    code_post = models.CharField(max_length=30, blank=True, verbose_name='Code post')
    name = models.CharField(max_length=30, null=True, blank=True)
    slug = models.SlugField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.post)

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    contact_1 = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    domicile = models.CharField(max_length=30, null=True, blank=True, default='')
    contact_2 = models.CharField(max_length=8, null=True, blank=True)
    phone_fix = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return '{} '.format(self.contact_1)

# ==============================================
#                  MODELE GISCONSULTING4
#                        END
# ==============================================
