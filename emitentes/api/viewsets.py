from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from emitentes.api import serializers
from emitentes import models


class EmitenteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.EmitenteSerializer
    queryset = models.Emitente.objects.all()
