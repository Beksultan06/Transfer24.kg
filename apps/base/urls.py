from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.base.views import BaseAPI, ServicesAPI

router = DefaultRouter()
router.register(r'base', BaseAPI, basename='base')
router.register(r'services', ServicesAPI, basename='services')

urlpatterns = [

]

urlpatterns += router.urls