from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from dj_rest_auth.views import PasswordResetConfirmView

schema_view = get_schema_view(
    openapi.Info(
        title="Authors Haven API",
        default_version='v1',
        description="Authors Haven API Project",
        contact=openapi.Contact(email="test@test.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/users/", include("users.urls")),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/v1/auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path("api/v1/profiles/", include("profiles.urls")),
    path("api/v1/articles/", include("articles.urls")),
    path("api/v1/ratings/", include("ratings.urls")),
    path("api/v1/bookmarks/", include("bookmarks.urls")),
    path("api/v1/responses/", include("responses.urls")),
    path("api/v1/elastic/", include("search.urls")),
]

admin.site.site_header = "Authors Haven API Admin"
admin.site.title = "Authors Haven API Admin Portal"
admin.site.index_title = "Welcome to Authors Haven API Portal"
