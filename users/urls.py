from .views import UserView
from core.urls import viewset_path


urlpatterns = [
    viewset_path(UserView, ""),
]
