import os
import sys
import warnings

import django

from django.conf import settings


warnings.simplefilter("always", DeprecationWarning)


DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "django.contrib.auth",
        "django.contrib.sites",
        "django_states",
    ],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
    SITE_ID=1,
    SECRET_KEY="notasecret",
    MIDDLEWARE_CLASSES=[],
    MIGRATION_MODULES={
        'auth': None,
        'contenttypes': None,
    }
)

if not settings.configured:
    settings.configure(**DEFAULT_SETTINGS)


# Compatibility with Django 1.7"s stricter initialization
if hasattr(django, "setup"):
    django.setup()


def runtests(*test_args):
    from django.test.runner import DiscoverRunner

    failures = DiscoverRunner(
        verbosity=2,
    ).run_tests(["tests"])

    sys.exit(failures)


if __name__ == "__main__":
    runtests()
