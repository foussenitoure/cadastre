

# =================================
#         ULRS GISCONSULTING
#             END
# =================================
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from  .import views
# from django.conf.urls import url


app_name = 'contacts'

urlpatterns = [
      path('admin/', admin.site.urls),
      path('contacts/', include('contacts.urls', namespace='contacts')),
      # path('signup/', views.signup, name='signup'),
]
