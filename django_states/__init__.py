#: The version list
VERSION = (2, 0, 0)

#: The actual version number, used by python (and shown in sentry)
__version__ = ".".join(map(str, VERSION))

default_app_config = 'django_states.apps.StateAppConfig'
