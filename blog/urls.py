from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
] + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
