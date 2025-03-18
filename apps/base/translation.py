from modeltranslation.translator import TranslationOptions, register
from apps.base.models import Base, Services, Settings, Tariffs, End, ServicesTrans

@register(Base)
class BaseTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description"
    )

@register(Services)
class ServecesTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )

@register(Tariffs)
class TariffsTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "type",
    )

@register(ServicesTrans)
class ServicesTransTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )

@register(End)
class EndTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )

@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = (
        'about', 'tarif', 'review', 'contact', 'title',
        'services', 'description', 'name', 'number', 'email',
        'send', 'info', 'location', 'pick', 'enter', 'tariff',
        'pick_up_date', 'phone', 'order', 'our_services', 'sviper',
        'drivers', 'business', 'event', 'video', 'support', 'text'
    )
