# Generated by Django 5.1.2 on 2024-11-29 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0004_productimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimage",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="apps.product",
            ),
        ),
    ]
