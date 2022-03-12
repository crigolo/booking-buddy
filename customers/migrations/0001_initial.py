# Generated by Django 4.0.1 on 2022-02-05 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("cell", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
