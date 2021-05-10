from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.decorators import action

from emitentes.api import serializers
from emitentes import models


class EmitenteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmitenteSerializer
    queryset = models.Emitente.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)


class NFeEmiteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NFeEmiteSerializer
    queryset = models.Emitente.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)


class NFCeEmiteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NFCeEmiteSerializer
    queryset = models.Emitente.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)


class CTeEmiteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CTeEmiteSerializer
    queryset = models.Emitente.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)


class MDFeEmiteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MDFeEmiteSerializer
    queryset = models.Emitente.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)


class CertificadoA1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CertificadoA1Serializer
    queryset = models.Emitente.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)
