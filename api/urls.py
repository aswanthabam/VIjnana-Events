from django.urls import path, include

urlpatterns = [
    path("cq/", include("api.cq.urls")),
    path("th/", include("api.th.urls")),
]
