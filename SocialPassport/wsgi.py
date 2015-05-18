"""
WSGI config for SocialPassport project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SocialPassport.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)