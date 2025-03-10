from django.contrib import admin
from apps.base.models import Base, Services, Tariffs
# Register your models here.
admin.site.register(Base)
admin.site.register(Services)
admin.site.register(Tariffs)