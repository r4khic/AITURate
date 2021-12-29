from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=30)
    s_name = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
