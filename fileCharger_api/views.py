from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import FileUploadParser
from rest_framework import status

from fileCharger_api import serializers
from fileCharger_api import models

# from fileCharger_api import serializers

class DatasetView(APIView):
    """ Endpoint Save Data and """

    # serializer_class = serializers.FileChargerSerializers
    parser_classes = (FileUploadParser,)

    def get(self, request):
        """ Return list and register Dataset """
        list_api = {

            'method': 'Usaremos GET, POST, PATCH, PUT, DELETE',
            'observation': 'Brinda control de la API'
        }

        return Response(list_api, status.HTTP_200_OK)
    
    def post(self, request):
        """ Save File information CSV """
        if request.FILES:
            csv = request.FILES.get('filename', none)
        
            print(csv)

        
        

        return Response('mensaje')
        

        
class RowsView(APIView):
    pass