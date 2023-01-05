from .views import AccountView
from core.urls import viewset_path


urlpatterns = [
    viewset_path(AccountView, ""),
]
