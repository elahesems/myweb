from django.db import models
# from __future__ import unicode_literals
# Create your models here.


class Main(models.Model):
    name= models.CharField(max_length=30)
    about= models.TextField()
    fb= models.CharField(max_length=30)
    tw= models.CharField(max_length=30)
    yt= models.CharField(max_length=30)
    gh= models.CharField(max_length=30)
    tell= models.CharField(max_length=30)
    link= models.CharField(max_length=30)



    set_name= models.CharField(max_length=30)

    def __str__(self):
        return self.set_name + " | " + str(self.pk)