from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Base(models.Model):
    title = models.CharField(
        max_length=155,verbose_name='Заголовок'
    )
    description = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='base', verbose_name='Фото'
    )
    links = models.URLField(
        verbose_name='Сыылка',
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Главная'

class Services(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Услуги'

class Tariffs(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    image = models.ImageField(
        upload_to='tariffs',
        verbose_name='Фото'
    )
    type = models.CharField(
        max_length=155,
        verbose_name='Тип'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Тарифы'

class Email(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    tariff = models.CharField(
        max_length=155,
        verbose_name='Тарифы'
    )
    date = models.CharField(
        max_length=255,
        verbose_name='Дата'
    )
    phone_number = models.CharField(
        max_length=155,
        verbose_name='Номер телефона'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Обратный связ'

class Contact(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    phone_number = models.CharField(
        max_length=25,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Контакты'