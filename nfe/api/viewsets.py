from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from nfe.api.serializers import NfeSerializer
from nfe.models import Nfe


def enviar_nfe(data):
    if type(data) == dict:
        # processar json-dict, gerar xml, assinar, validar e enviar a Sefaz via assíncrona

        respond = {
            "http_code": 202,
            "cnpj_emitente": "07504505000132",
            "status_nfe": "processando_autorizacao",
            "mensagem": "Processando autorização"
        }
    else:
        respond = {
            "http_code": 400,
            "codigo": "json_parse_error",
            "mensagem": "Bad Request - O texto recebido não é um formato json válido"
        }

    return respond


class NfeViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Nfe.objects.all()
    serializer_class = NfeSerializer
