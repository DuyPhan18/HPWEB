from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    product_price = models.DecimalField(max_digits = 10, decimal_places=0)
    product_quantity = models.IntegerField(default=0)
    product_category = models.CharField(max_length=100)
    product_image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.product_name
    def add_product(self, **data):
        new_product = Products(**data)
        new_product.save()
    def update_product(self, data):
        self.product_name = data.get('product_name', self.product_name)
        self.product_desc = data.get('product_name', self.product_desc)
        self.product_price = data.get('product_name', self.product_price)
        self.self.product_quantity = data.get('product_name', self.product_quantity)
        self.product_category = data.get('product_name', self.product_category)
        self.product_image = data.get('product_name', self.product_image)
        self.date = data.get('product_name', self.date)
        self.status = data.get('product_name', self.status)
        self.save()
        return f"Sản phẩm {self.product_name} đã được cập nhật thành công."

    def delete_product(self):
        if self.status != "True":
            self.delete()
            return "Sản phẩm đã được xóa thành công."