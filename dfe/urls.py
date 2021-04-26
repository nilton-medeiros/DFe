from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from emitentes.api.viewsets import EmitenteViewSet
from nfe.api.viewsets import NfeViewSet

router = routers.DefaultRouter()
router.register(r'emitente', EmitenteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('nfe/', NfeViewSet.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
