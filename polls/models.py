from django.db import models

from django.contrib.auth.models import User


class Data(models.Model):
    pin = models.IntegerField(blank=False, null=False)
    user = models.OneToOneField(User, blank=False, null=False)
    address = models.CharField(blank=False,null=False,max_length=100)




