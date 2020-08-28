from django.db import models
# from __future__ import unicode_literals
# Create your models here.


class Main(models.Model):
    name= models.TextField()
    about= models.TextField()

    def __str__(self):
        return self.name