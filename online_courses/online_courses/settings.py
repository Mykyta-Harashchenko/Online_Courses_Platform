import os
from pathlib import Path
import environ
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Определяем базовую директорию проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Загружаем переменные окружения
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Настройки Cloudinary
cloudinary.config(
    cloud_name=env('CLD_NAME'),
    api_key=env('CLD_API_KEY'),
    api_secret=env('CLD_API_SECRET')
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLD_NAME'),
    'API_KEY': env('CLD_API_KEY'),
    'API_SECRET': env('CLD_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Отладка загрузки Cloudinary API-ключей
print("Cloudinary Config:", env('CLD_NAME'), env('CLD_API_KEY'), env('CLD_API_SECRET'))

# Безопасность
SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

# Приложения Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'app_auth',
    'warrior',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'online_courses.urls'

TEMPLATES = [
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

WSGI_APPLICATION = 'online_courses.wsgi.application'

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Локализация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические и медиа файлы
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'

# Авторизация
LOGIN_URL = "app_auth/login"
LOGIN_REDIRECT_URL = 'app_auth:profile'

# Email настройки
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Настройки автоматического создания полей в базе данных
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
