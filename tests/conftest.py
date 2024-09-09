import os
from pathlib import Path

from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent

def pytest_configure():
    settings.configure(
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "nigerian_only",
        ],
        MIDDLEWARE=[
            "nigerian_only.middleware.NigeriansOnlyMiddleware",
        ],
        ROOT_URLCONF="nigerian_only.urls",
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
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
        ],

        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "db.sqlite3",
            }
        },
        GEOIP_PATH = os.path.join(BASE_DIR, 'tests/geoip'), # Path('GeoLite2-Country.mmdb'),
        WHITELISTED_COUNTRIES = ['NG'],  # , 'GB'],
        WHITELISTED_IPS=['127.0.0.1'],
    )

