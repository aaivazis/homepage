# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
"""
Django settings for homepage

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# python imports
import os
import homepage

# folder definitions
BASE = os.path.abspath(os.path.join(homepage.home, os.pardir))
WEB = os.path.join(BASE, 'web')
STATIC_DIR = os.path.join(BASE, 'static')
# important folder definitions
TEMPLATES = os.path.join(WEB, 'templates')
RESOURCES = os.path.join(WEB, 'resources')
UPLOADS = os.path.join(STATIC_DIR, 'uploads')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = open(os.path.expanduser('~homepage/SECRET_KEY')).readline().strip()

#WSGI_APPLICATION = 'conf.wsgi'

ALLOWED_HOSTS = ['104.236.200.165', 'alec.aivazis.com']
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# end of file
