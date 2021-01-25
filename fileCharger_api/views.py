# Django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status

# Local
from fileCharger_api.models import Dataset, Client, Row
from fileCharger_api.serializers import DatasetListSerializer, DatasetLoadSerializer, RowListSerializer


# from fileCharger_api import serializers

class DatasetView(APIView):
    """ Endpoint para grabar y visualizar la información del Dataset
    Metodo GET :    Permite visualizar la ruta Path de los archivos que se han almacedados en Servidor
    Metodo POST :   Guarda Archivos en el servidor, al momento de recibir el archivo es necesario especificar el nombre por URL
    """
    parser_classes = (FileUploadParser,)

    def get(self, request):
        """ Permite listar todos los registro del Dataset """
        datasets = Dataset.objects.all()
        list_datasets = DatasetListSerializer(datasets, many=True)

        return Response(list_datasets.data, status=status.HTTP_200_OK)
    
    def post(self, request, filename, format=None):
        """ Guardar los archivos en servidor, y guarda path en BD"""
        file_obj = request.FILES
        
        if 'file' not in request.data:
            code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
            error = {'message': 'No se envió ningún archivo'}
            
            return Response(error, code)

        try:
            """ Guardar archivo """
            csv = Dataset(name=filename,file_name=file_obj['file'])
            csv.save()
            dataset_id = Dataset.objects.last()
            client_id = Client.objects.get(pk=1)
            endpoint = 1
            """ Guardar registro en Row"""
            row = Row(dataset_id=dataset_id, client_id=client_id, point=endpoint)
            row.save()
            message = {'message': 'Archivo cargado correctamente'}

            return Response(message, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            print(e)
            raise e

        return Response(status=status.HTTP_201_CREATED)


class RowsView(APIView):
    """ Endpoint para visualizar registros del Row
        Metodo GET :    Permite visualizar la lista de registros de Row, al igual que filtrar los registro por medio de query params
        query params:   dataset_id (requerido), name
    """
    def get(self, request):
        """ Permite listar todos los registro del Rows """
        rows = Row.objects.all()   
        listserializer = RowListSerializer(rows, many=True)
        return Response(listserializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        """ Recibe un query params para filtrar listado de Row"""
        dataset = self.request.query_params.get('dataset_id', None)
        name = self.request.query_params.get('name', None)
        rows = Row.objects.all()     

        if dataset:
            filter_row = self.request.query_params.get('dataset_id')
            list_filter = rows.filter(dataset_id=filter_row)
            print(list_filter)
            lista = RowListSerializer(list_filter)            

        elif name:
            filter_row = self.request.query_params.get('name')
            client_id = Client.objects.filter(name=filter_row)
            list_filter = rows.filter(client_id=filter_row)
            lista = RowListSerializer(list_filter)
            return Response(lista.data, status=status.HTTP_200_OK)
        
        else:
            message = {'message': 'Es requerido el dataset_id'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        return Response(lista.data, status=status.HTTP_200_OK)
