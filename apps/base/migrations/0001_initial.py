# Generated by Django 5.1.7 on 2025-03-14 12:31

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
                (
                    "links",
                    models.URLField(blank=True, null=True, verbose_name="Сыылка"),
                ),
            ],
            options={
                "verbose_name_plural": "Главная",
            },
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=155, verbose_name="Заголовка")),
                ("phone_number", models.IntegerField(verbose_name="Номер телефона")),
                ("email", models.EmailField(max_length=254, verbose_name="Почта")),
            ],
            options={
                "verbose_name_plural": "Контакты",
            },
        ),
        migrations.CreateModel(
            name="Email",
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
                (
                    "description",
                    models.CharField(max_length=155, verbose_name="Описание"),
                ),
                ("tariff", models.CharField(max_length=155, verbose_name="Тарифы")),
                ("date", models.CharField(max_length=255, verbose_name="Дата")),
                (
                    "phone_number",
                    models.CharField(max_length=155, verbose_name="Номер телефона"),
                ),
            ],
            options={
                "verbose_name_plural": "Обратный связ",
            },
        ),
        migrations.CreateModel(
            name="Services",
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
                (
                    "title_ru",
                    models.CharField(
                        max_length=155, null=True, verbose_name="Заголовка"
                    ),
                ),
                (
                    "title_ky",
                    models.CharField(
                        max_length=155, null=True, verbose_name="Заголовка"
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "description_ru",
                    models.TextField(null=True, verbose_name="Описание"),
                ),
                (
                    "description_ky",
                    models.TextField(null=True, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name_plural": "Услуги",
            },
        ),
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
