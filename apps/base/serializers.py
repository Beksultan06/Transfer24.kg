from rest_framework import serializers
from apps.base.models import Base, Email, Services, Tariffs, Contact
import re

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['title', 'description', 'image']


class ServisecSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id','title', 'description']

class TariffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariffs
        fields = ['title', 'image']

# Сериализатор
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

    def validate_phone_number(self, value):
        """Валидация номера телефона (пример для международного формата)"""
        if not re.match(r'^\+?\d{10,15}$', value):
            raise serializers.ValidationError("Некорректный номер телефона.")
        return value

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"  