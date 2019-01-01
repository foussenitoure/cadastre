from django.db import models
from django.contrib.gis.db import models as gis_models
import random
from random import  randint
# from django.db.models.AutoField
from django.db.models.signals import pre_save
from .utils import unique_matricule_id_generator, \
    unique_product_id_generator, \
    unique_order_id_generator, \
    unique_person_id_generator
from django.forms import widgets

# Create your models here.

# ==============================================

#                  MODELE ORGANIZATION
# #                        START
# ==============================================
class organization(models.Model):

    STATUS = (
        ('Association', 'Association'),
        ('Ong', 'ONG'),
        ('Parti Politique', 'Parti Politique'),
    )
    status = models.CharField(max_length=50, choices=STATUS, default='------')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nom de Organisation')
    sigle = models.CharField(max_length=50, blank=True, null=True, verbose_name='Sigle')
    image = models.ImageField(upload_to='Logo', null=True, blank=True, verbose_name='Logo Organization')
    Contact = models.IntegerField( null=True, blank=True, verbose_name='Telephone Fixe')
    phone = models.IntegerField(null=True, blank=True, verbose_name='Telephone mobile')
    door = models.IntegerField( null=True, blank=True, verbose_name='Porte')
    street = models.IntegerField( null=True, blank=True, verbose_name='Rue')

    def __str__(self):
        return'{} {} {}'.format(self.name, self.sigle, self.phone)

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='profil', null=True, blank=True, verbose_name='Photo_person')
    GENRE = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autres'),
    )
    CATEGORY = (
        ('G', 'Grande'),
        ('M', 'Moyenne'),
        ('P', 'Petite'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY, default='CLIENT')
    sex = models.CharField(max_length=20, choices=GENRE, default='Homme')
    # category = models.CharField(max_length=20, choices=CATEGORY, default='Grande')
    code_person = models.CharField(max_length=30, blank=True, verbose_name='Code person')
    prenom = models.CharField(max_length=30, null=True, blank=True)
    nom = models.CharField(max_length=30, null=True, blank=True)
    date_naissance = models.DateField(auto_now_add=True)
    contact_1 = models.IntegerField(null=True, blank=True)
    contact_2 = models.CharField(max_length=8, null=True, blank=True)
    nationalite = models.CharField(max_length=30, null=True, blank=True)
    nina = models.CharField(max_length=30, null=True, blank=True)
    domicile = models.CharField(max_length=30, null=True, blank=True, default='Lafiabougou')
    email = models.EmailField(max_length=100, null=True, blank=True)
    alias = models.CharField(verbose_name='alias', max_length=30, null=True, blank=True)
    profession = models.CharField(max_length=30, null=True, blank=True)
    tutuelle = models.CharField(max_length=30, null=True, blank=True)
    telephonique_fix = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return'{} {} {}'.format(self.prenom, self.nom, self.contact_1)

def pre_save_person_id(instance, sender, *args, **kwargs):
    if not instance.code_person:
            instance.code_person = unique_person_id_generator(instance)

pre_save.connect(pre_save_person_id, sender=Person)

class Post(models.Model):
    NAME = (
        ('President', 'President'),
        ('Secretaire General', ' Secretaire General'),
        ('Secretaire Administratif ', 'Secretaire Administratif '),
        ('Tresorier ', 'Tresorier'),)
    name = models.CharField(max_length=100, choices=NAME, default='CLIENT')
    CATEGORY = (
        ('Membre', 'Membre'),
        ('Sympathisant', ' Sympathisant'),)
    category = models.CharField(max_length=100, choices=CATEGORY, default='CLIENT')
    duration = models.DurationField()

    def __str__(self):
        return '{} {} {}'.format(self.name, self.category, self.duration)

class cotisation(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Titulaire command', )
    payer = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    reliquat = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    confirm = models.BooleanField(default=False)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Poste',)
    activite = models.ForeignKey('Activite', on_delete=models.CASCADE, verbose_name='Activites Investissement',)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return'{} {} {}'.format(self.id, self.reliquat, self.total)

class Activite(models.Model):
    id = models.AutoField(primary_key=True)
    start_act = models.DateTimeField()
    reliquat_invest = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    montant_invest = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    confirm = models.BooleanField(default=False)
    end_act = models.DateTimeField()
    localisation = models.DecimalField()
    image = models.ImageField(upload_to='img_act', null=True, blank=True, verbose_name='Images Activites')
    publish = models.BooleanField(default=True)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.montant_invest, self.image)

# ==============================================
#                   MODELE ORGANIZATION
# # #                        END
# ==============================================



# ==============================================

#                  MODELE LOCALISATION
#                        START
# ==============================================

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    id_reg = models.IntegerField(null=True, blank=True)
    name_reg = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return'{}'.format(self.name_reg)


class Cercle(models.Model):
    id = models.AutoField(primary_key=True)
    id_cer = models.IntegerField(null=True, blank=True)
    name_cer = models.CharField(max_length=30, null=True, blank=True)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name_cer)


class Commune(models.Model):
    id = models.AutoField(primary_key=True)
    id_com = models.IntegerField(null=True, blank=True)
    name_com = models.CharField(max_length=30, null=True, blank=True)
    id_cercle = models.ForeignKey('Cercle', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name_com)

class Village(models.Model):
    id = models.AutoField(primary_key=True)
    code_village = models.BigIntegerField(null=True, blank=True)
    id_village = models.PositiveIntegerField(null=True, blank=True)
    name_village = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    latitude = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    id_commune = models.ForeignKey('Commune', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name_village)

# ==============================================
#                  MODELE LOCALISATION
#                        END
# ==============================================