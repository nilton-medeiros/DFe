from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from emitentes.api import serializers
from emitentes import models


class EmitenteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmitenteSerializer
    queryset = models.Emitente.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        user = request.user
        if user.is_authenticated:
            queryset = queryset.filter(user_id=user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
