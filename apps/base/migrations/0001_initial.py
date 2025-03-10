# Generated by Django 5.1.7 on 2025-03-09 10:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Base",
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
                ("title", models.CharField(max_length=155, verbose_name="Заголовок")),
                (
                    "title_ru",
                    models.CharField(
                        max_length=155, null=True, verbose_name="Заголовок"
                    ),
                ),
                (
                    "title_ky",
                    models.CharField(
                        max_length=155, null=True, verbose_name="Заголовок"
                    ),
                ),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "description_ru",
                    ckeditor.fields.RichTextField(null=True, verbose_name="Описание"),
                ),
                (
                    "description_ky",
                    ckeditor.fields.RichTextField(null=True, verbose_name="Описание"),
                ),
                ("image", models.ImageField(upload_to="base", verbose_name="Фото")),
            ],
            options={
                "verbose_name_plural": "Главная",
            },
        ),
    ]
