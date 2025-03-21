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

class End(models.Model):
    title = models.CharField(
        max_length=155,verbose_name='Заголовок'
    )
    description = RichTextField(
        verbose_name='Описание'
    )
    links = models.URLField(
        verbose_name='Сыылка',
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Конец'

class ServicesTrans(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='base', verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Услуги Трансапорта'

class Settings(models.Model):
    about = models.CharField(
        max_length=155,
        verbose_name=r'Заголовка о нас'
    )
    services = models.CharField(
        max_length=155,
        verbose_name=r'Заголовка о услуги'
    )
    tarif = models.CharField(
        max_length=155,
        verbose_name=r'Заголовка о тариф'
    )
    review = models.CharField(
        max_length=155,
        verbose_name=r'Заголовка о отзывы'
    )
    contact = models.CharField(
        max_length=155,
        verbose_name='Заголовка контактов'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    number = models.CharField(
        max_length=155,
        verbose_name='Номер телефона'
    )
    email = models.CharField(
        max_length=155,
        verbose_name='почта'
    )
    send = models.CharField(
        max_length=155,
        verbose_name='Отправить'
    )
    info = models.CharField(
        max_length=155,
        verbose_name='Заголовка Информаций'
    )
    location = models.CharField(
        max_length=155,
        verbose_name='Заголовка локаций'
    )
    watapp = models.URLField(
        verbose_name='Ссылка на ватсап'
    )
    telegram = models.URLField(
        verbose_name='Ссылка на телеграм'
    )
    insta = models.URLField(
        verbose_name='Ссылка на Истаграм'
    )
    phone_number_2 = models.CharField(
        max_length=155,
        verbose_name='Ссылка на номер телефона'
    )
    
    pick = models.CharField(
        max_length=155,
        verbose_name='Подобрать '
    )
    enter = models.CharField(
        max_length=155,
        verbose_name='Введите пункт назначения'
    )
    tariff = models.CharField(
        max_length=155,
        verbose_name='Тариф'
    )
    pick_up_date = models.CharField(
        max_length=155,
        verbose_name='Дата получения'
    )
    phone = models.CharField(
        max_length=155,
        verbose_name='Телефон'
    )
    order = models.CharField(
        max_length=155,
        verbose_name='Заказ'
    )
    our_services = models.CharField(
        max_length=155,
        verbose_name='Наши услуги'
    )
    sviper = models.CharField(
        max_length=155,
        verbose_name='Что говорят наши клиенты'
    ) 
    drivers = models.CharField(
        max_length=155,
        verbose_name='Водители'
    )
    business = models.CharField(
        max_length=155,
        verbose_name='Бизнес встречи'
    )
    event = models.CharField(
        max_length=155,
        verbose_name='События'
    )
    video = models.CharField(
        max_length=155,
        verbose_name='Видеообзоры'
    )
    support = models.CharField(
        max_length=155,
        verbose_name='Поддержать'
    )
    text = models.CharField(
        max_length=155,
        verbose_name='Текстовые обзоры'
    )
    banner_link = models.URLField(
        verbose_name='Ссылка'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Главные Настройки'