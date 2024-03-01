from django.urls import path, include

from django.contrib import admin

admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
import home.views,stati.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", home.views.index, name="index"),
    path("stat/",stati.views.index,name="statitics"),
    path("admin/", admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)