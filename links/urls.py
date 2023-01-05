from .views import LinkView
from core.urls import viewset_path


urlpatterns = [
    viewset_path(LinkView, ""),
]
