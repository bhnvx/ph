from django.contrib import admin
from django.urls import path, include

from links.views import redirect_origin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path('<encode_link>/', redirect_origin),
]
