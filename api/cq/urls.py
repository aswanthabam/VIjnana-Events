from django.urls import path, include
from .views import InitializationView
urlpatterns = [
    path("initialize/", InitializationView.as_view(), name="initialize"),
]
