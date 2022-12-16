from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url


urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]