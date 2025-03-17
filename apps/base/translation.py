from modeltranslation.translator import TranslationOptions, register
from apps.base.models import Base, Services, Tariffs, End, ServicesTrans

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