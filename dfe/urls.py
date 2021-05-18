from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from emitentes.api.viewsets import (EmitenteViewSet, NFeEmiteViewSet, NFCeEmiteViewSet, CTeEmiteViewSet,
                                    MDFeEmiteViewSet, CertificadoA1ViewSet)
from nfe.api.viewsets import NfeViewSet

router = routers.DefaultRouter()
router.register(r'nfes', NfeViewSet)
router.register(r'emitentes', EmitenteViewSet)
router.register(r'emitentes/nfe', NFeEmiteViewSet)
router.register(r'emitentes/nfce', NFCeEmiteViewSet)
router.register(r'emitentes/cte', CTeEmiteViewSet)
router.register(r'emitentes/mdfe', MDFeEmiteViewSet)
router.register(r'emitentes/certificado', CertificadoA1ViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
