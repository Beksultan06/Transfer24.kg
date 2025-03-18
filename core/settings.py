from pathlib import Path
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-7t7b8wb9^fu(*&00!2+%(wc(*!=4=rv&ia)fxv2imn65ht80y3"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'modeltranslation',
    'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "ckeditor",
    "corsheaders",
    "drf_yasg",
    "apps.base",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware", 
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English')),
]

LANGUAGE_CODE = 'ru'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "dist")],  # Указываем путь к фронту
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

TIME_ZONE = "Asia/Bishkek"

USE_I18N = True
USE_TZ = True

# STATIC_URL = "/assets/"
# # STATIC_ROOT = BASE_DIR / "/static/"

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "dist", "assets"),  # Подключаем assets напрямую
# ]

STATIC_URL = "/assets/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "dist", "assets"),
]



# STATICFILES_DIRS удаляем, так как "dist" уже в TEMPLATES['DIRS']

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 300,
        'width': 800,
    },
}

JAZZMIN_SETTINGS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-success",
    "navbar": "navbar-success navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-success",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'nurlanuuulubeksultan@gmail.com'
EMAIL_HOST_PASSWORD = 'ztdwjizhqxbboncb'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
ADMIN_EMAIL = 'grazy9891@gmail.com'

# CORS Настройки
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://fc3d-158-181-248-104.ngrok-free.app",
    "http://192.168.31.5",
]

CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]

CORS_ALLOW_HEADERS = [
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",  # Добавляем локальный бэкенд
    "https://fc3d-158-181-248-104.ngrok-free.app",
    "http://192.168.31.5",
]
