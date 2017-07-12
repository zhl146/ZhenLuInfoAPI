from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^posts/', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('projects.urls'))
]
