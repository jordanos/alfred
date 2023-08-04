from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="AI Customer Service API",
        default_version="v1",
        description="REST API To Create AI bots",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jordanoswork2021@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

API_PATH = "api/v1"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: redirect(f"{API_PATH}")),
    path(
        f"{API_PATH}",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        f"{API_PATH}/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path(f"{API_PATH}/auth/", include("authentication.urls"), name="auth"),
    path(f"{API_PATH}/agents/", include("agent.urls"), name="agents"),
    path(f"{API_PATH}/chats/", include("chat.urls"), name="chats"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
