
from django.db import models


class Main_table(models.Model):
    dis_class = models.CharField(max_length=30,default='')
    dis_clss_2= models.CharField(max_length=30,default='')

    def __str__(self):
        return self.dis_class
