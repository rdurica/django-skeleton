import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from application.api.urls import api_urls

urlpatterns = [
    path('admin', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += api_urls

admin.site.site_header = 'Example'
admin.site.index_title = 'Modules'
admin.site.site_title = 'Example'
