from django.db import models

# Create your models here.
class Voucher(models.Model):
    voucher_name = models.CharField(max_length=50)
    v_quantity = models.IntegerField()
    v_discount = models.IntegerField()
    status = models.BooleanField(default=False)
    
    @classmethod
    def create_voucher(cls,data):
        new_v = cls.objects.create(**data)
        return new_v