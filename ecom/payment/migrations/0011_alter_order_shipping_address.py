# Generated by Django 5.0.3 on 2024-03-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0010_alter_order_shipping_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="shipping_address",
            field=models.TextField(blank=True, max_length=15000, null=True),
        ),
    ]
