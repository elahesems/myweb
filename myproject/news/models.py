from django.db import models
# from __future__ import unicode_literals
# Create your models here.


class News(models.Model):
    categories=(
        ('book','book'),
        ('football','football'),
        ('science','science'),
        ('general','general'),
    )
    name= models.CharField(max_length=50)
    short_txt= models.TextField()
    body_txt= models.TextField()
    date= models.DateTimeField()
    time= models.CharField(max_length=12,default="00:00")
    picname= models.TextField()
    picurl  = models.TextField(default="-")
    writer= models.CharField(max_length=50)
    catname= models.CharField(max_length=50,choices=categories,default='general')
    catid= models.IntegerField(default=0)
    show= models.IntegerField(default=0)



    def __str__(self):
        return self.name