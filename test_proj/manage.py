#!/usr/bin/env python
import os
import sys

try:
    import settings  # Assumed to be in the same directory.
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing {}. "
                     "It appears you've customized things.\nYou'll have to run django-admin.py, "
                     "passing it your settings module.\n".format(repr(__file__)))
    sys.exit(1)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
