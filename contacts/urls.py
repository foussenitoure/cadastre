from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


from django.contrib import admin
from django.urls import path, include
from  .import views
from django.conf.urls import url


app_name = 'contacts'

urlpatterns = [
      path('', include('contacts.urls')),
]

