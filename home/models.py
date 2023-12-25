from django.db import models
from product.models import Products

# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    