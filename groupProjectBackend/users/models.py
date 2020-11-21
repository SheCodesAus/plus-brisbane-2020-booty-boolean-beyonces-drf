from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    image = models.URLField(max_length=200, default="https://picsum.photos/id/1025/200/300")
    location = models.CharField(max_length=80)
    fav = models.ManyToManyField(Product)
    # Dont need to create fields for add_fav and remove_fav in the model, they can just exist in the serializer


# username, email, password are part of AbstractUser

    def __str__(self):
        return self.username