from rest_framework import serializers

class ApiFileChargerSerializers(serializers.Serializer):
    """  """
    name = serializers.CharField(max_length=95)
    