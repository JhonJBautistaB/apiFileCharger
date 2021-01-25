from rest_framework import serializers
from fileCharger_api.models import Dataset, Row

class DatasetListSerializer(serializers.Serializer):
    name = serializers.CharField()
    file_name = serializers.CharField()
    date = serializers.DateTimeField()

class DatasetLoadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=45)
    file_name = serializers.FileField(allow_empty_file=False, use_url=True)

    def create(self, data):
        return Dataset.objects.create(**data)


class RowListSerializer(serializers.Serializer):
    dataset_id = serializers.CharField()
    client_id = serializers.CharField()
    point = serializers.IntegerField()


