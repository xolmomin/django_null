# Generated by Django 5.1.2 on 2024-11-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0002_category_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_premium",
            field=models.BooleanField(db_default=False),
        ),
    ]
