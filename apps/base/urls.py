from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.base.views import BaseAPI, EmailViewSet, ServicesAPI, TariffsAPI

router = DefaultRouter()
router.register(r'base', BaseAPI, basename='base')
router.register(r'services', ServicesAPI, basename='services')
router.register(r'tariffs', TariffsAPI, basename='tariffs')
router.register(r'feedback', EmailViewSet, basename='feedback')

urlpatterns = [

]

urlpatterns += router.urls