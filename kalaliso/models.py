from django.db import models

# Create your models here.
# !/usr/bin/python
#  -*- coding: latin-1 -*-

# reload(sys)
# sys.setdefaultencoding('utf-8')
# import os, sys

# from import reload
from django.db.models import FloatField
# from django.utils.encoding import python_2_unicode_compatible
from functools import update_wrapper
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.base import ModelBase
from django.views.decorators.cache import never_cache
# from django.contrib.gis.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import utc
from django.db.models import Avg
import psycopg2
import datetime
import sys

class Person(models.Model):
    # image = models.ImageField(upload_to='photos/profil%Y/%m/%d', null=True, blank=True, verbose_name='Photo_commande')
    STATUS = (
        ('Client', 'CLIENT'),
        ('Ouvrier', 'OUVRIER'),
        ('Apprenti', 'APPRENTI'),
        ('Fournisseur', 'FOURNISSEUR'),
        ('Company', 'COMPANY'),)

    status = models.CharField(max_length=20, choices=STATUS, default='CLIENT')
    SEX = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autres'),
    )
    CATEGORIE = (
        ('G', 'Grande'),
        ('M', 'Moyenne'),
        ('P', 'Petite'),
    )
    sex              = models.CharField(max_length=20, choices=SEX, default='Homme')
    prenom           = models.CharField(max_length=30, null=True, blank=True)
    nom              = models.CharField(max_length=30, null=True, blank=True)
    contact          = models.IntegerField(primary_key=True)
    email            = models.EmailField(max_length=100, null=True, blank=True)
    categorie        = models.CharField(max_length=20, choices=CATEGORIE, default='Grande')
    domicile         = models.CharField(max_length=30, null=True, blank=True, default='Lafiabougou')
    create_at        = models.DateField(auto_now=False)
    # update_at        = models.DateField(auto_now=False)

    def __str__(self):
        return'{} {} {}'.format(self.prenom, self.nom, self.contact)


class Mesure(models.Model):

    person_mesure   = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Client')
    # mesure_client   = models.ManyToManyField('Produit', verbose_name='Mesure Par Produit')
    # person          = models.ManyToManyField('Person')
    coude           = models.FloatField(null=True, blank=True)
    epaule          = models.FloatField(null=True, blank=True)
    manche          = models.FloatField(null=True, blank=True)
    tour_manche     = models.FloatField(null=True, blank=True)
    taille          = models.FloatField(null=True, blank=True)
    poitrine        = models.FloatField(null=True, blank=True)
    longueur_boubou = models.FloatField(null=True, blank=True)
    longueur_patanlon = models.FloatField(null=True, blank=True)
    fesse           = models.FloatField(null=True, blank=True)
    ceinture        = models.FloatField(null=True, blank=True)
    cuisse          = models.FloatField(null=True, blank=True)
    patte           = models.FloatField(null=True, blank=True)
    create_at       =  models.DateTimeField(auto_now_add=True)
    update_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{}'.format(self.person_mesure)

class Produit(models.Model):
    NOM_PRODUIT         = (
        ('Boubou', 'Boubou'),
        ('Grand Boubou', 'Grand Boubou'),
        ('Chemise Complet', 'Chemise Complet'),
        ('Chemise Manche Long', 'Chemise Manche Long'),
        ('Chemise Manche Court', 'Chemise Manche Court'),
        ('Pagne Jupe', 'Pagne Jupe'),
        ('Pagne Complet', 'Pagne Complet'),
        ('Pagne Maniere', 'Pagne Maniere'),
        ('Patanlon', 'Patanlon'),
        ('Tenu Scolaire', 'Tenu Scolaire'),
        ('Tenu Securite', 'Tenu Securite'),
        ('AUTRES', 'AUTRES'),)

    nom_produit         = models.CharField(max_length=25, choices=NOM_PRODUIT, default='')
    image               = models.ImageField(upload_to='photos/profil%Y/%m/%d', null=True, blank=True, verbose_name='img_command')

    def __str__(self):
        return'{}'.format(self.nom_produit,)

class Commande(models.Model):
    command_person  = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Titulaire command', )
    products        = models.ManyToManyField('Produit', verbose_name='list_commande')
    reception       = models.DateTimeField(auto_now_add=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    price_total     = models.DecimalField(max_digits=5, decimal_places=2)
    taxe            = models.DecimalField(max_digits=5, decimal_places=2)
    remise          = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    quantite        = models.DecimalField(max_digits=5, decimal_places=2)
    rendez_vous     = models.DateTimeField(auto_now_add=False)
    livre           = models.BooleanField(default=False)
    create_at       =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return'{}'.format(self.id)

