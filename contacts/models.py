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
    DOMAINE    = (
        ('GEOMATIQUE', 'GEOMATIQUE'),
        ('BTP',        'BTP'),
        ('ARTISANAT', 'ARTISANAT'),)

    post       = models.TextField(max_length=10000, blank=True, verbose_name='post')
    title      = models.CharField(max_length=200, blank=True, verbose_name='title')
    name_dom   = models.CharField(max_length=10, choices=DOMAINE, null=True, blank=True,)
    address    = models.ForeignKey('Address', on_delete=models.CASCADE, verbose_name='Address')
    image      = models.ImageField(upload_to='posted', null=True, blank=True, verbose_name='Photo_commande')
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

class Address(models.Model):
    id         = models.AutoField(primary_key=True)
    email      = models.EmailField(max_length=100, null=True, blank=True)
    domicile   = models.CharField(max_length=100, null=True, blank=True, default='')
    phone1     = models.CharField(max_length=8,null=True, blank=True)
    phone2     = models.CharField(max_length=8, null=True, blank=True)
    phone_fix  = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.phone1)

# ==============================================
#                  MODELE GISCONSULTING4
#                        END
# ==============================================
