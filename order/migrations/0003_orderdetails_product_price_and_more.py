# Generated by Django 4.2.7 on 2023-12-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0002_rename_total_quantity_choose_orderdetails_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderdetails",
            name="product_price",
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="orderdetails",
            name="total_price",
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
