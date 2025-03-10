from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.base.views import BaseAPI, ServicesAPI, TariffsAPI

router = DefaultRouter()
router.register(r'base', BaseAPI, basename='base')
router.register(r'services', ServicesAPI, basename='services')
router.register(r'tariffs', TariffsAPI, basename='tariffs')

urlpatterns = [

]

urlpatterns += router.urls