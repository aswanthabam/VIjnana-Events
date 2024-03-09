from django.urls import path, include, re_path

from django.contrib import admin

admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
import home.views,statistics.views
from django.views.static import serve


urlpatterns = [
    path("v1/", home.views.index, name="index"),
    path("v1/statistics/",statistics.views.index,name="statitics"),
    path("v1/admin/", admin.site.urls),
    path("api/", include("api.urls")),
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT})
]
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, {"document_root":settings.STATIC_ROOT})