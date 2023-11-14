# Generated by Django 4.2.7 on 2023-11-14 01:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_order_orderitem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("name", models.CharField(max_length=50)),
                ("tittle", models.CharField(max_length=70)),
                ("image", models.ImageField(upload_to="media")),
                ("paragraph", models.CharField(max_length=1000)),
            ],
        ),
    ]