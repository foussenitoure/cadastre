from django.db import models
from django.contrib.gis.db import models as gis_models
# from django.contrib.gis.db.models
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
#                  MODELE CADASTRE
#                        START
# ==============================================

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    STATUS              = (
        ('PERSONNE PHYSIQUE',   'Personne physique'),
        ('PERSONNE MORALE',    'Personne morale'),)
    status              = models.CharField(max_length=30, choices=STATUS, null=True, blank=True,)
    SEXE = (
        ('HOMME', 'Homme'),
        ('FEMME', 'Femme'),)
    sexe                = models.CharField(max_length=10, choices=SEXE, null=True, blank=True,)
    nom                 = models.CharField(max_length=50, null=True, blank=True,)
    prenom              = models.CharField(max_length=50, null=True, blank=True,)
    matricule           = models.CharField(max_length=50, blank=True,)
    photo               = models.ImageField(upload_to='photos/identite', null=True,)
    contact             = models.CharField(max_length=8, null=True, blank=True,)
    n_cin               = models.CharField(max_length=50, null=True, blank=True,)
    nina                = models.CharField(max_length=50, null=True, blank=True,)
    profession          = models.CharField(max_length=50, null=True, blank=True,)
    rcimm               = models.CharField(max_length=50, null=True, blank=True,)
    nif                 = models.CharField(max_length=50, null=True, blank=True,)
    siege_social        = models.CharField(max_length=50, null=True, blank=True, )
    responsable         = models.CharField(max_length=50, null=True, blank=True,)
    email               = models.EmailField(max_length=50, null=True, blank=True,)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return ('{}-{}-{}').format(self.nom, self.prenom, self.contact)

def pre_save_matricule_id(instance, sender, *args, **kwargs):
        if not instance.matricule:
            instance.matricule = unique_matricule_id_generator(instance)

pre_save.connect(pre_save_matricule_id, sender=Contact)


class Parcel(models.Model):
    id = models.AutoField(primary_key=True)
    Nature = (
        ('BATI',   'Bati'),
        ('NON BATIE',    'Non Bati'),)
    nature = models.CharField(max_length=30, choices=Nature,)
    contact = models.ManyToManyField('Contact')
    geom = gis_models.MultiPolygonField(srid=32642, blank=True, null=True)
    superficie = models.PositiveIntegerField()
    perimeter = models.PositiveIntegerField()
    dr = models.ForeignKey('Droit', on_delete=models.CASCADE, verbose_name='Droits Réels')
    doc_adm = models.ForeignKey('Document_Administration', on_delete=models.CASCADE, verbose_name='Document Administratif')
    code = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{}-{}').format(self.code, self.nature)

class Droit(models.Model):
    id = models.AutoField(primary_key=True)
    DR = (
        ('LA PROPRIETE DES BIENS IMMEUBLES', 'Propriete des biens immeubles'),
        ('USUFRUIT DES MEMES BIENS', 'Usufruit des memes biens'),
        ('LES DROITS USAGE ET HABITATION', 'les Droits usage et habitation'),
        ('EMPHYTEOSE', 'emphyteose'),
        ('LE DROIT DE SUPERFICIE', 'droit de superficie'),
        ('LES SERVITUDES OU SERVICES FONCIERS', 'les servitudes ou services fonciers'),
        ('ANTICHRESE', 'anthichrese'),
        ('LES PRIVILEGES ET HYPOTHEQUE', 'les Privileges et hypotheque'),)

    dr = models.CharField(max_length=50, choices=DR, blank=True)

    def __str__(self):
       return ('{}').format(self.dr)

class Recette_fiscale(models.Model):
    id = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE, verbose_name='TITULAIRE')
    parcel_id = models.ForeignKey('Parcel', on_delete=models.CASCADE, verbose_name='Parcelle concerne')
    code_fiscale = models.CharField(max_length=30,)
    impot = models.CharField(max_length=30,)
    taxes = models.CharField(max_length=30,)
    redevance = models.CharField(max_length=30,)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{}').format(self.code_fiscale)

class Document_Administration(models.Model):
    id = models.AutoField(primary_key=True)
    DOC_ADM = (
            # ('RAS', 'ras'),
            # ('DROITS REELS', 'Droits réels'),
            ('DROIT COUTUMIER', 'Droit coutumier'),
            ('TITRE FONCIER', 'Titre Foncier'),
            ('TITRE PROVISOIRE', 'Titre provisoire'),
            ("ATTESTATION D'EXPLOITATION", "Attestation d'Exploitation"),)
    da = models.CharField(max_length=30, choices=DOC_ADM)

    def __str__(self):
        return ('{}').format(self.da)

class Region(models.Model):
        id = models.AutoField(primary_key=True)
        id_reg = models.IntegerField(null=True, blank=True)
        name_reg = models.CharField(max_length=30, null=True, blank=True)

        def __str__(self):
            return '{}'.format(self.name_reg)

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
#                  MODELE CADASTRE
#                        END
# ==============================================



