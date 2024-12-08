import os
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent

SECRET_KEY: str = os.getenv('SECRET_KEY')

DEBUG: bool = eval(os.getenv('DEBUG'))

ALLOWED_HOSTS: list[str] = [
    '127.0.0.1',
]

INTERNAL_IPS: list[str] = [
    '127.0.0.1',
]

CORS_ALLOWED_ORIGINS: list[str] = [
    'http://localhost:3000',
    'http://127.0.0.1:8000',
]

INSTALLED_APPS: list[str] = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'corsheaders',
    'debug_toolbar',
    'django_filters',
    'drf_yasg',

    'products',
    'users',
    'carts',
    'orders',
]

MIDDLEWARE: list[str] = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF: str = 'exzoo_backend.urls'

TEMPLATES: list[dict] = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION: str = 'exzoo_backend.wsgi.application'

DATABASES: dict = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_USER_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

AUTH_PASSWORD_VALIDATORS: list[dict] = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE: str = 'en-EN'

TIME_ZONE: str = 'Europe/Moscow'

USE_I18N: bool = True

USE_TZ: bool = True

STATIC_URL: str = 'static/'

MEDIA_URL: str = 'media/'
MEDIA_ROOT: Path = BASE_DIR / 'media'

FIXTURE_DIRS: list = [
    'fixtures',
]

DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'

REST_FRAMEWORK: dict = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

AUTH_USER_MODEL: str = 'users.User'
EMAIL_HOST: str = 'smtp.gmail.com'
EMAIL_PORT: int = 587
EMAIL_USE_TLS: bool = True
EMAIL_HOST_USER: str = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD: str = os.getenv('EMAIL_HOST_PASSWORD')

DOMAIN: str = os.getenv('DOMAIN')
SITE_NAME: str = 'Exzoo'

DJOSER: dict = {
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'PASSWORD_CHANGE_EMAIL_CONFIRMATION': True,
    'ACTIVATION_URL': 'account/activation/{uid}/{token}/',
    'PASSWORD_RESET_CONFIRM_URL': 'account/reset-password/{uid}/{token}/',
    'SERIALIZERS': {
        'user': 'users.serializers.UserSerializer',
        'current_user': 'users.serializers.UserSerializer',
    },
}

SWAGGER_SETTINGS: dict = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
