
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",include("accounts.urls",namespace="accounts")),
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path('file/', include("file_upload.urls")),
    path('file/', include("file_download.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
