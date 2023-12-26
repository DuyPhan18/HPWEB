from django.db import models
from product.models import Products
from django.utils import timezone
# Create your models here.

class Promotes(models.Model):
    products = models.ManyToManyField(Products, related_name="product")
    promote_name = models.CharField(max_length=100)
    discount = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return self.promote_name
    @classmethod
    def add_promote(cls, data):
        # Logic để thêm một khuyến mãi mới
        new_promote = cls.objects.create(**data)
        return new_promote