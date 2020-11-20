from django.db import models

# Create your models here.

class Product(models.Model):
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    os = models.TextField(default="")
    model_tech =  models.TextField(default="")
    spec1 = models.TextField()
    spec2 = models.TextField()
    spec3 = models.TextField()
    spec4 = models.TextField()
    spec5 = models.TextField()
    spec6 = models.TextField(default="")
    image = models.URLField()
    price = models.IntegerField()
    justification = models.TextField(default="")
    supplier1 = models.URLField()
    supplier2 = models.URLField()
    overview = models.TextField(default="")


    

