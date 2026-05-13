
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", 'your-fallback-secret-key')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'


ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'backend']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "user",
    "card",
    "rest_framework",
    "corsheaders",
    "django_eventstream"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # CORS должен идти как можно выше, перед CommonMiddleware
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
]

ROOT_URLCONF = "project.urls"

 

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates/"],
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

WSGI_APPLICATION = "project.wsgi.application"
ASGI_APPLICATION = "project.asgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db_data" / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True


USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "django_static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# JWT token settings
JWT_COOKIE_NAME = "access_token"
JWT_EXPIRATION_HOURS = 24

REST_FRAMEWORK = {'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'], 'DEFAULT_AUTHENTICATION_CLASSES': [
        'user.services.auth.CustomJWTAuth',
        'rest_framework.authentication.SessionAuthentication',  # для админки и Browsable API
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}


# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]

CORS_ALLOW_CREDENTIALS = True

# Дополнительные настройки CORS для cookie
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_EXPOSE_HEADERS = [
    'set-cookie',
]

SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

# EVENTSTREAM_ALLOW_ORIGIN = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
#     "http://localhost:8000",
#     "http://127.0.0.1:8000",
# ]
EVENTSTREAM_ALLOW_ORIGIN = ["http://localhost",]

def get_eventstream_channels(request):
    """
    Возвращает список разрешённых каналов для SSE.
    Обрабатывает запросы вида: /events/?channel=crew-1 или /events/?channels=crew-1
    """
    channels = []
    # Получаем каналы из параметров channel или channels
    channel_param = request.GET.get('channel') or request.GET.get('channels')
    if channel_param:
        # Если передан один канал (строка), добавляем его
        if isinstance(channel_param, str):
            # Если несколько каналов через запятую, разбиваем
            channel_list = [ch.strip() for ch in channel_param.split(',')]
            channels.extend(channel_list)
        # Если передано несколько каналов (список)
        elif isinstance(channel_param, list):
            channels.extend(channel_param)
    
    # Разрешаем все каналы вида crew-* для упрощения (в продакшене лучше добавить проверку)
    # Фильтруем только crew-* каналы для безопасности
    filtered_channels = [ch for ch in channels if ch and ch.startswith('crew-')]
    
    return filtered_channels

EVENTSTREAM_CHANNELS = get_eventstream_channels