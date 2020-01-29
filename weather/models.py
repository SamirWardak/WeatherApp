from django.db import models


class City(models.Model):
    name = models.CharField(unique=True,max_length=30)

    def __str__(self):
        return self.name

