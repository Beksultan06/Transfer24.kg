from modeltranslation.translator import TranslationOptions, register
from apps.base.models import Base, Services

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
        "description"
    )
