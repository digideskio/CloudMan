import os
import sys

sys.path.append('/var/www')
sys.path.append('/var/www/export')

os.environ['DJANGO_SETTINGS_MODULE'] = 'export.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


