from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length = 10000)
    uuid = models.CharField(max_length = 10)
    #creating a database names url with 2 tables, 1st is link & 2nd is uuid

