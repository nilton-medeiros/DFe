from rest_framework import status, viewsets
from rest_framework.authentication import (
    BasicAuthentication,
    TokenAuthentication
)
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from emitentes import models
from emitentes.api import serializers


class EmitenteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmitenteSerializer
    queryset = models.Emitente.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)

    def get_serializer_class(self):
        serializers_choices = {
            'nfe_emit': serializers.NFeEmiteSerializer,
            'nfce_emit': serializers.NFCeEmiteSerializer,
            'cte_emit': serializers.CTeEmiteSerializer,
            'mdfe_emit': serializers.MDFeEmiteSerializer
        }
        return serializers_choices.get(self.action, serializers.EmitenteSerializer)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        user = request.user
        if user.is_authenticated:
            queryset = queryset.filter(user_id=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user_id=self.resquest.user)

    def partial_update(self, request, *args, **kwargs):
        return super(EmitenteViewSet, self).partial_update(request, *args, **kwargs)

    @action(detail=True, url_path='nfe-emit', name="nfe-emit", methods=['put'])
    def nfe_emit(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @action(detail=True, url_path='nfce-emit', name="nfce-emit", methods=['put'])
    def nfce_emit(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @action(detail=True, url_path='cte-emit', name="cte-emit", methods=['put'])
    def cte_emit(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @action(detail=True, url_path='mdfe-emit', name="mdfe-emit", methods=['put'])
    def mdfe_emit(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
