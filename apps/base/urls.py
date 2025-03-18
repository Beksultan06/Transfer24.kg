from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.base.views import BaseAPI, EmailViewSet, ServicesAPI, TariffsAPI, FeedbackViewSet, EndAPI, ServicesTransAPI, SettingsAPI

router = DefaultRouter()
router.register(r'base', BaseAPI, basename='base')
router.register(r'services', ServicesAPI, basename='services')
router.register(r'tariffs', TariffsAPI, basename='tariffs')
router.register(r'feedback', EmailViewSet, basename='feedback')
router.register(r'contact', FeedbackViewSet, basename='contact')
router.register(r'end', EndAPI, basename='end')
router.register(r'servicestrans', ServicesTransAPI, basename='servicestrans')
router.register(r"settings", SettingsAPI, basename='settings')



urlpatterns = [

]

urlpatterns += router.urls