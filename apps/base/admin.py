from django.contrib import admin
from apps.base.models import Base, Services, Tariffs, Contact, ServicesTrans, End, Settings
# Register your models here.
admin.site.register(Base)
admin.site.register(Services)
admin.site.register(Tariffs)
admin.site.register(Contact)
admin.site.register(ServicesTrans)
admin.site.register(End)
admin.site.register(Settings)