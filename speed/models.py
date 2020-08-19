from django.db import models
from django.contrib.auth.models import User



class Client(models.Model):
    client_D = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=30)
    client_phone = models.IntegerField()
    client_address = models.CharField(max_length=200)

    def __str__(self):
        return self.client_name
