# Generated by Django 5.1.7 on 2025-03-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_services"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tariffs",
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
                ("title", models.CharField(max_length=155, verbose_name="Заголовка")),
                ("image", models.ImageField(upload_to="tariffs", verbose_name="Фото")),
            ],
            options={
                "verbose_name_plural": "Тарифы",
            },
        ),
    ]
