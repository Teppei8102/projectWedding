from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-nr7=-hl=2$v_m*d6fm)a*k*ra94cabaer*u_r5_ad&42(blh=3"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_bootstrap5",
    "appWedding",
]

AUTH_USER_MODEL = 'appWedding.EntryForm'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "projectWedding.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR) + '/templates'],
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

WSGI_APPLICATION = "projectWedding.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

LANGUAGE_CODE = "ja"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

PREFECTURES = [
    ("北海道"  ,"北海道"  ),
    ("青森県"  ,"青森県"  ),
    ("岩手県"  ,"岩手県"  ),
    ("宮城県"  ,"宮城県"  ),
    ("秋田県"  ,"秋田県"  ),
    ("山形県"  ,"山形県"  ),
    ("福島県"  ,"福島県"  ),
    ("茨城県"  ,"茨城県"  ),
    ("栃木県"  ,"栃木県"  ),
    ("群馬県"  ,"群馬県"  ),
    ("埼玉県"  ,"埼玉県"  ),
    ("千葉県"  ,"千葉県"  ),
    ("東京都"  ,"東京都"  ),
    ("神奈川県","神奈川県"),
    ("新潟県"  ,"新潟県"  ),  
    ("富山県"  ,"富山県"  ),  
    ("石川県"  ,"石川県"  ),  
    ("福井県"  ,"福井県"  ),  
    ("山梨県"  ,"山梨県"  ),  
    ("長野県"  ,"長野県"  ),  
    ("岐阜県"  ,"岐阜県"  ),  
    ("静岡県"  ,"静岡県"  ),  
    ("愛知県"  ,"愛知県"  ),  
    ("三重県"  ,"三重県"  ),  
    ("滋賀県"  ,"滋賀県"  ),  
    ("京都府"  ,"京都府"  ),  
    ("大阪府"  ,"大阪府"  ),  
    ("兵庫県"  ,"兵庫県"  ),  
    ("奈良県"  ,"奈良県"  ),  
    ("和歌山県","和歌山県"),
    ("鳥取県"  ,"鳥取県"  ),  
    ("島根県"  ,"島根県"  ),  
    ("岡山県"  ,"岡山県"  ),  
    ("広島県"  ,"広島県"  ),  
    ("山口県"  ,"山口県"  ),  
    ("徳島県"  ,"徳島県"  ),  
    ("香川県"  ,"香川県"  ),  
    ("愛媛県"  ,"愛媛県"  ),  
    ("高知県"  ,"高知県"  ),  
    ("福岡県"  ,"福岡県"  ),  
    ("佐賀県"  ,"佐賀県"  ),  
    ("長崎県"  ,"長崎県"  ),  
    ("熊本県"  ,"熊本県"  ),  
    ("大分県"  ,"大分県"  ),  
    ("宮崎県"  ,"宮崎県"  ),  
    ("鹿児島県","鹿児島県"),
    ("沖縄県"  ,"沖縄県"  ),  
]