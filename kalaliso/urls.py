from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


from django.contrib import admin
from django.urls import path, include
from  .import views
from django.conf.urls import url


app_name = 'kalaliso'

urlpatterns = [
    # path('admin/', admin.site.urls),
      path('', include('kalaliso.urls')),
]