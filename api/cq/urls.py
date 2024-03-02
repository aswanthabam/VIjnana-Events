from django.urls import path, include
from .views import InitializationView, QuestionAPIView, SubmissionAPIView, LeaderboardView
urlpatterns = [
    path("initialize/", InitializationView.as_view(), name="initialize"),
    path("get-question/", QuestionAPIView.as_view(), name="get-question"),
    path("add-question/", QuestionAPIView.as_view(), name="add-question"),
    path("submit/", SubmissionAPIView.as_view(), name="submit"),
    path("leaderboard/", LeaderboardView.as_view(), name="leaderboard"),
]
