from django.shortcuts import render
from apps.base.models import Base, Services
from apps.base.serializers import BaseSerializer, ServisecSerializers

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
# Create your views here.

class BaseAPI(GenericViewSet,
              mixins.ListModelMixin):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer

class ServicesAPI(GenericViewSet,
                  mixins.ListModelMixin):
    queryset = Services.objects.all()
    serializer_class = ServisecSerializers