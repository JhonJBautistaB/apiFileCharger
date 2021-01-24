from rest_framework import serializers

class FileChargerSerializers(serializers.Serializer):
    """ Input Acces Documentation """
    name = serializers.CharField(max_length=45)
    file_name = serializers.FileField()
