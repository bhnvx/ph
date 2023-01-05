from types import ModuleType
from typing import Optional

from django.urls import include, path
from rest_framework.routers import DefaultRouter


def viewset_path(
    viewset, prefix: str, basename: Optional[str] = None
) -> tuple[ModuleType, Optional[bool], Optional[bool]]:
    router = DefaultRouter()
    router.register(prefix, viewset, basename=basename or prefix)
    return path("", include(router.urls))


urlpatterns = [
    path('users/', include('users.urls')),
    path('accounts/', include('accounts.urls')),
    path('links/', include('links.urls')),
]
