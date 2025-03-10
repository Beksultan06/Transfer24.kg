from rest_framework import serializers
from apps.base.models import Base, Services, Tariffs

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