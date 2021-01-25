from django.db import models
from django.utils.timezone import now


class Dataset(models.Model):
    """ Creation DB Dataset"""
    name = models.CharField(max_length=45)
    file_name = models.FileField(upload_to='files/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def get(self):
        return self.pk
    


class Row(models.Model):
    dataset_id = models.ForeignKey(Dataset, related_name='dataset', on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, related_name='client', on_delete=models.CASCADE)
    point = models.IntegerField()


class LoggerAPI(models.Model):
    ipaddress = models.IntegerField
    date = models.DateTimeField(auto_now=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.ipaddress
    