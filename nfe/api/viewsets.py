from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class NfeViewSet(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        json_nfe = request.data
        print(json_nfe)
        print(type(json_nfe))
        response = {
            "sucesso": True
        }
        return Response(response, status=200)
