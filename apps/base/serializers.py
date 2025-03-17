from rest_framework import serializers
from apps.base.models import Base, Email, Services, Tariffs, Contact, ServicesTrans, End
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
        fields = ['title', 'image', 'type']

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class ServicesTransSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServicesTrans
        fields = ['title', 'description', 'image']

class EndSerializers(serializers.ModelSerializer):
    class Meta:
        model = End
        fields = ['title', 'description', 'links']