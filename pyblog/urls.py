from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
# from  contacts import views
# from  . import views  program, genFooterTable, genBodyTable, genHeaderTable
from reportlab.platypus import Table
from contacts import views
# from  reportlab.pdfgen views  genFooterTable, genBodyTable, genHeaderTable

app_name = 'contacts'

urlpatterns = [

      # path('home/', views.HomePageView, name='homepage'),
      # path('home/', HomePageView.as_view(), name='homepage'),
      path('admin/', admin.site.urls),
      path('', views.homepage, name='homepage'),
      path('upload/', views.image_upload_view, name='upload'),
      path('upload/detail/<int:upload_id>/', views.vuesimg, name='vues_img'),

      path('login/', views.user_login, name='login'),
      path('logout/', views.logout_user, name='logout'),
      path('register/', views.register_user, name='register'),
      path('edit/profile/', views.edit_profile, name='edit_profile'),
      path('change/password/', views.change_password, name='change_password'),

      path('post/', views.post, name='post'),
      path('post/detail/<int:post_id>/', views.post_detail, name='post_detail'),

]
