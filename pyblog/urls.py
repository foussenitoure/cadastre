from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
# from  contacts import views
# from  . import views  program, genFooterTable, genBodyTable, genHeaderTable
from reportlab.platypus import Table
from contacts import views
from django.conf import settings
from django.conf.urls.static import static
# from  reportlab.pdfgen views  genFooterTable, genBodyTable, genHeaderTable

app_name = 'contacts'

urlpatterns = [

# =================================
#         ULRS KALALISO
#             START
# =================================
      path('admin/', admin.site.urls),
      path('maps/', views.maps, name='maps'),
      path('info/', views.info, name='detail_info'),
      path('', views.post, name='post'),
      path('<int:post_id>', views.detail, name='detail'),
      # path('address/', views.address, name='address'),
      # path('upload/', views.image_upload_view, name='upload'),
      # path('upload/detail/<int:upload_id>/', views.vuesimg, name='vues_img'),

      # path('(?P<id>[0-9]+)/upload_detaitl/$', views.upload_detail, name='upload_detail'),
      # path('upload_detail/<int:id>/', views.upload_detail, name='upload_detail'),
      # path('upload/<int:id>/', views.image_upload_view_detail, name='upload-detail'),
      # path('product/<int:id>/', views.product_detail, name='product-detail'),
      # path('', views.homepage, name='add_post'),

      # path('login/', views.user_login, name='login'),
      # path('logout/', views.logout_user, name='logout'),
      # path('register/', views.register_user, name='register'),
      # path('profile/', views.profile, name='profile'),
      # path('edit/profile/', views.edit_profile, name='edit_profile'),
      # path('change/password/', views.change_password, name='change_password'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
