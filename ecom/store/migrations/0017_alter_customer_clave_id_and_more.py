# Generated by Django 5.0.3 on 2024-03-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0016_service_service_collect_service_service_deposit_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="clave_id",
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name="discount",
            name="discount_fix_or_percentage",
            field=models.CharField(
                choices=[("Fixed", "Fixed"), ("Percentage", "Percentage")],
                max_length=20,
                null=True,
            ),
        ),
    ]