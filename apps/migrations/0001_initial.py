# Generated by Django 5.1.2 on 2024-10-28 12:51

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_comment="Bu ismi kiritadigan joy", max_length=255
                    ),
                ),
                ("price", models.IntegerField(db_default=1000)),
            ],
            options={
                "verbose_name_plural": "Categories",
                "default_manager_name": "ikkinchi",
            },
            managers=[
                ("ikkinchi", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("passport_series", models.CharField(max_length=2, null=True)),
                ("passport_number", models.CharField(max_length=7, null=True)),
            ],
            options={
                "verbose_name": "Mahsulot",
                "db_tablespace": "valijon_tablespace",
            },
        ),
    ]
