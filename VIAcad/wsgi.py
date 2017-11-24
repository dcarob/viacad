"""
WSGI config for VIAcad project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
path= os.path.expanduser('~/VIAcad')
if path not in sys.path:
	sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VIAcad.settings")

application = StaticFilesHandler(get_wsgi_application())
