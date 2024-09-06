import os
from pathlib import Path

import django, sys
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent

settings.configure(
    SECRET_KEY='django-insecure-**jx#59um8^yeryatw3@*ch9&fu^@3&9x9bh2f5fb!hp-_p7l^',
    # Application definition
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "nigerian_only",
    ],
    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "nigerian_only.middleware.NigerianOnlyMiddleware",
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
    GEOIP_PATH = os.path.join(BASE_DIR, 'geoip'), # Path('GeoLite2-Country.mmdb'),
    WHITELISTED_COUNTRIES = ['NG'],  # , 'GB'],
    # Define allowed IPs during tests
    ALLOWED_TEST_IPS=['127.0.0.1'],
)
django.setup()
from django.test.runner import DiscoverRunner

test_runner = DiscoverRunner(verbosity=2)

failures = test_runner.run_tests(["."])
if failures:
    sys.exit(failures)
