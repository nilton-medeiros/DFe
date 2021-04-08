from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


class NfeViewSet(ModelViewSet):
    queryset = None
    serializer_class = None

    @action(detail=False, methods=['POST'])
    def enviar(self, request):
        return {
            'status': 'Autorizado',
            'codigo_status': '100',
            'motivo': 'Autorizado o uso de NFe 0000232',
        }
