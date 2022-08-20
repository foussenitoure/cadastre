from django.contrib import admin
from django.forms import Textarea
from django.db import models

# from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ()
    # list_filter = ("status",)
    # search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}
admin.site.register(CustomUser, CustomerUserAdmin)