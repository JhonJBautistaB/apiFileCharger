from django.db import models
from django.utils.timezone import now


class Dataset(models.Model):
    """ Creation DB Dataset"""
    name = models.CharField(max_length=45)
    file_name = models.FileField(upload_to='files/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
    

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        """Return name"""
        return name

class Row(models.Model):
    dataset_id = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    point = models.IntegerField()

class LoggerAPI(models.Model):
    ipaddress = models.IntegerField
    date = models.DateTimeField(auto_now=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

