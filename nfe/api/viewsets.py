from typing import Dict, Union

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


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


class NfeViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    # Recebe o JSON da NFe, gera o XML, Assina, Valida e envia à Sefaz se não houver erro
    def post(self, request):
        json_file = request.data
        response = enviar_nfe(data=json_file)
        # print(response)
        http_code = response['http_code']
        del response['http_code']
        return Response(response, status=http_code)
