from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from contacts import views
# from  . import views  program, genFooterTable, genBodyTable, genHeaderTable
from reportlab.platypus import Table
# from  .import views
# from  reportlab.pdfgen views  genFooterTable, genBodyTable, genHeaderTable
from django.conf import settings
from django.conf.urls.static import static


app_name = 'contacts'

urlpatterns = [

      # =================================
      #         ULRS CADASTRE
      #             START
      # =================================
      path('', views.home, name='home'),
      path('workspaces/', views.workspaces, name='workspaces'),
      path('profil_pdf/', views.profil_pdf, name='profil_pdf'),
      path('parcel/', views.parcel, name='parcel'),
      path('parcels/detail/<int:parcel_id>/', views.parcel_detail, name='parcel_detail'),
      path('contact/', views.contact, name='adresses'),
      path('contact/detail/<int:contact_id>/', views.contact_detail, name='contact-detail'),
      path('about/', views.about, name='about'),
      path('login/', views.user_login, name='login'),
      path('logout/', views.logout_user, name='logout'),
      path('register/', views.register_user, name='register'),
      path('edit/profile/', views.edit_profile, name='edit_profile'),
      path('change/password/', views.change_password, name='change_password'),
      path('region/', views.region, name='region'),
      path('cercle/', views.cercle, name='cercle'),
      path('arrondissement/', views.arrondissement, name='arrondissement'),
      path('commune/', views.commune, name='commune'),
      path('village/', views.village, name='village'),
      # =================================
      #         ULRS CADASTRE
      #             END
      # =================================

]
