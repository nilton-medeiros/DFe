from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from emitentes.api import serializers
from emitentes import models


class EmitenteViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.EmitenteSerializer
    queryset = models.Emitente.objects.all()
