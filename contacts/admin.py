from django.contrib import admin
from django.forms import Textarea
from django.db import models

# from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from .models import *

admin.site.register(Post)



admin.site.register(Address)