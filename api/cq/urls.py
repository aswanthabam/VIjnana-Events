from django.urls import path, include
from .views import InitializationView, QuestionAPIView, SubmissionAPIView
urlpatterns = [
    path("initialize/", InitializationView.as_view(), name="initialize"),
    path("get-question/", QuestionAPIView.as_view(), name="get-question"),
    path("add-question/", QuestionAPIView.as_view(), name="add-question"),
    path("submit/", SubmissionAPIView.as_view(), name="submit"),
]
