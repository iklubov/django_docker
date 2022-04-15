

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('redirect_urls/', include('redirect_urls.urls')),
    path('admin/', admin.site.urls),
]