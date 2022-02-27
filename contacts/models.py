from django.db import models
from django.forms import forms
from django.contrib.gis.db import models as gis_models
import random
from random import randint
# from django.db.models.AutoField
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


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

    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )

    content    = models.TextField(verbose_name='Post')
    status     = models.IntegerField(choices=STATUS, default=0)
    slug       = models.SlugField(max_length=200, unique=True)
    title      = models.CharField(max_length=200, blank=True, verbose_name='Title')
    author     = models.ForeignKey(User, on_delete= models.CASCADE,related_name='Blog_posts')
    domaine   = models.CharField(max_length=10, choices=DOMAINE, null=True, blank=True,)
    email      = models.EmailField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    domicile   = models.CharField(max_length=100, null=True, blank=True, default='')
    phone1     = models.CharField(max_length=8,null=True, blank=True)
    phone2     = models.CharField(max_length=8, null=True, blank=True)
    phone_fix  = models.CharField(max_length=15, null=True, blank=True)
    image      = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Photo')


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}'.format(self.title)



# ==============================================
#                  MODELE GISCONSULTING4
#                        END
# ==============================================
