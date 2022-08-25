from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    mobile = models.CharField(max_length=11)
    address = models.CharField(max_length=250)
    pin_code = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=250)