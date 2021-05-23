from django.contrib import admin
import os
from django.contrib import admin
from django.contrib import auth
from django import forms
from django.utils import timezone
# from suit.admin import SortableTabularInline
from kalaliso.models import Person,  Mesure, Commande, Produit


class PersonAdmin(admin.ModelAdmin):
    save_on_top = True
    models = Person
    fields = ['status',
              'prenom',
              'nom',
              'sex',
              'categorie',
              'domicile',
              'contact',
              'email',
              'create_at',]

    # exclude = ['update_at']

    list_display =   (
                      'status',
                      'prenom',
                      'nom',
                      'sex',
                      'categorie',
                      'domicile',
                      'contact',
                      'email',)

    # ordering       = ['created_at']
    # date_hierarchy = 'created_at'
    list_filter      = ['status']
    search_fields    = ['contact']
admin.site.register(Person, PersonAdmin)

class ProduitAdmin(admin.ModelAdmin):
    # save_on_top = True
    models = Produit
    fields = ['nom_produit', 'image',]

   #  exclude = ['profession',
   # ]
   #  list_display = ('produit',)

    # ordering  = ['created_at']
    # date_hierarchy = 'created_at'
    # list_filter = ['produit']
    # search_fields = ['produit',]
admin.site.register(Produit, ProduitAdmin)


class MesureAdmin(admin.ModelAdmin):
    save_on_top = True
    model = Mesure
    fields = ['person_mesure',
              # 'mesure_modele',
              # 'mesure_client',
              'coude',
              'epaule',
              'manche',
              'tour_manche',
              'taille',
              'poitrine',
              'fesse',
              'longueur_boubou',
              'longueur_patanlon',
              'patte',
              ]
    #
    # exclude = ['ceinture',
    #            'cuisse',
    #            'create_at',
    #            'update_at',]

    list_display = (
                'person_mesure',
                # 'mesure_modele',
                'coude',
                'epaule',
                'manche',
                'taille',
                'poitrine',
                'fesse',
                'longueur_boubou',
                'longueur_patanlon',
                'patte',)

    # ordering  = [']
    # date_hierarchy = ''
    # list_filter = []
    # search_fields = []
admin.site.register(Mesure, MesureAdmin)

class CommandeAdmin(admin.ModelAdmin):
    save_on_top = True
    models = Commande
    fields = ['command_person', 'products', 'quantite',
              'price', 'taxe', 'remise','price_total', 'reception',
               'rendez_vous',
               ]

    exclude = [
               'create_at',
               'livre',
               ]

    list_display = (
               'command_person',
               'quantite',
               'price',
               'taxe',
               'remise',
               'price_total',
               # 'products',
               'rendez_vous',
               'reception',
               'create_at'
                )

    ordering = ['create_at']

    list_filter = []
    search_fields = []
admin.site.register(Commande, CommandeAdmin)