from django.shortcuts import render
from apps.base.models import Base, Services, Tariffs, Email
from apps.base.serializers import BaseSerializer, ServisecSerializers, TariffsSerializer, EmailSerializer

from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class BaseAPI(GenericViewSet,
              mixins.ListModelMixin):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer

class ServicesAPI(GenericViewSet,
                  mixins.ListModelMixin):
    queryset = Services.objects.all()
    serializer_class = ServisecSerializers

class TariffsAPI(GenericViewSet,
                  mixins.ListModelMixin):
    queryset = Tariffs.objects.all()
    serializer_class = TariffsSerializer

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        """Обрабатывает входящие запросы и отправляет email"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email_instance = serializer.save()

            # Отправка email
            self.send_feedback_email(email_instance)

            return Response(
                {"message": "Ваш запрос успешно отправлен!", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_feedback_email(self, email_instance):
        """Функция отправки email уведомления"""
        subject = f"Новая заявка: {email_instance.title}"
        message = (
            f"Описание: {email_instance.description}\n"
            f"Тариф: {email_instance.tariff}\n"
            f"Дата: {email_instance.date}\n"
            f"Номер телефона: {email_instance.phone_number}"
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  # От кого
            [settings.ADMIN_EMAIL],  # Кому отправлять
            fail_silently=False
        )