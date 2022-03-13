
from django.contrib import admin
from django.urls import path, include
# import settings and static first a képek feltöléséhez és a megjelenítéséhez
from django.conf import settings   
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('', include('first_site.urls')),
    path('admin/', admin.site.urls),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('tinymce/', include('tinymce.urls')),

]

urlpatterns += i18n_patterns (
    path('', include('first_site.urls')),
    path('members/', include('members.urls')),
    
)

# add this lines - képek feltöléséhez és megjelenítéséehz
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)