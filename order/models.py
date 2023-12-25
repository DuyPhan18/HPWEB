from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#lấy user hiện tại đang đăng nhập
def get_current_user():
    return User.objects.get(username='duyphan').id

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_current_user)
    total_bill =  models.DecimalField(max_digits=30, decimal_places=0)
    total_quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    @classmethod
    def create_order(cls, data):
        new_order = cls(**data)
        new_order.save()


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name="products", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits = 10, decimal_places=0)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    @classmethod
    def create_order_detail(cls, data):
        order_detail = cls(**data)
        order_detail.save()
