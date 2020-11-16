from django.db import models

# Create your models here.

class Product(models.Model):
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    spec1 = models.TextField()
    spec2 = models.TextField()
    spec3 = models.TextField()
    spec4 = models.TextField()
    spec5 = models.TextField()
    image = models.URLField()
    price = models.IntegerField()
    supplier1 = models.URLField()
    supplier2 = models.URLField()

