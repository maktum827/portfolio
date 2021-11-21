from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# to change the names of admin panel 
admin.site.site_header = 'Maktum Mishok Administration'
admin.site.site_title = 'Maktum Mishok Admin Panel'
admin.site.index_title = 'Welcome to Admin Panel'

# import views from blog
from apps.blog.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('apps.blog.urls')),
]

# For working media 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
