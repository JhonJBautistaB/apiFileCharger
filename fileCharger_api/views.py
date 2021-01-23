from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from fileCharger_api import serializers

class ApiFileChargerView(APIView):
    """"""
    serializers_class = serializers.ApiFileChargerSerializers

    def get(self, request, format=None):
        """ Return list register Dataset """
        list_api = {

            'method': 'Usaremos GET, POST, PATCH, PUT, DELETE',
            'observation': 'Brinda control de la API'
        }

        return Response(list_api)
    
    def post(self, request):
        """"""
        pass