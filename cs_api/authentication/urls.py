from django.urls import include, path

from .views import GitHubLogin, GoogleLogin

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path(
        "registration/",
        include("dj_rest_auth.registration.urls"),
    ),
    path("social/google/", GoogleLogin.as_view(), name="google_login"),
    path("social/github/", GitHubLogin.as_view(), name="github_login"),
]
