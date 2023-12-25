from django.db import models
from product.models import Products
# Create your models here.
class Promotes(models.Model):
    products = models.ManyToManyField(Products, related_name="product")
    promote_name = models.CharField(max_length=100)
    discount = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField()

    def __str__(self): 
        return self.promote_name