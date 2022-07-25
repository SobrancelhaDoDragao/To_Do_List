from django.db import models

class task(models.Model):

    name = models.CharField(max_length=140)
    status = models.IntegerField()
