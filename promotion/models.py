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
    @classmethod
    def update_promote(cls,instance, data):
        instance.products.set(data.get('products', instance.products.all()))
        instance.promote_name = data.get('promote_name', instance.promote_name)
        instance.discount = data.get('discount', instance.discount)
        instance.start_date = data.get('start_date', instance.start_date)
        instance.end_date = data.get('end_date', instance.end_date)
        instance.status = data.get('status', instance.status)
        instance.save()