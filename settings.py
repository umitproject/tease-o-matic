#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
## Author: Adriano Monteiro Marques <adriano@umitproject.org>
##
## Copyright (C) 2011 S2S Network Consultoria e Tecnologia da Informacao LTDA
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU Affero General Public License as
## published by the Free Software Foundation, either version 3 of the
## License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Affero General Public License for more details.
##
## You should have received a copy of the GNU Affero General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native',}
#DATABASES['mongodb'] = {'ENGINE': 'django_mongodb_engine', 'NAME' : 'teasewebsite',}
AUTOLOAD_SITECONF = 'indexes'


SITE_NAME = 'ICM'
SITE_DESCRIPTION = ''
SITE_COPYRIGHT = ''
GOOGLE_ANALYTICS_MODEL = True

ROOT_URLCONF = 'urls'
SITE_ID = 1

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ENVIRONMENT = os.environ.get('SERVER_SOFTWARE', '')
GAE = True
PRODUCTION = True
TEST = False

if ENVIRONMENT == '':
    # TODO: Figure how to check if running on prod in other environments
    GAE = False
elif ENVIRONMENT.startswith('Development'):
    PRODUCTION = False
elif ENVIRONMENT.startswith('GAETest'):
    TEST = True

EMAIL_SENDING_ACCOUNT = ""
EMAIL_REPLY_TO = ""
EMAIL_HOST = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_HOST_USER = ""
EMAIL_PORT = 25
EMAIL_USE_TLS = True

APPEND_SLASH = True


SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
#    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    #'django.contrib.sites',
    #'django.contrib.flatpages',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'mediagenerator',
    'simplesocial',
    'subscriptions',
    'django.contrib.admin',
    'google_analytics',
    'minicms',

    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',

    'mediagenerator.middleware.MediaMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'urlrouter.middleware.URLRouterFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'subscriptions.context_processors.config',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'


ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

URL_ROUTE_HANDLERS = (
    'minicms.urlroutes.PageRoutes',
)

ROOT_MEDIA_FILTERS = {
    'js': 'mediagenerator.filters.closure.Closure',
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

CLOSURE_COMPILER_PATH = os.path.join(os.path.dirname(__file__),
                                     '.webutils', 'compiler.jar')

YUICOMPRESSOR_PATH = os.path.join(os.path.dirname(__file__),
                                  '.webutils', 'yuicompressor.jar')

MEDIA_DEV_MODE = DEBUG
DEV_MEDIA_URL = '/devmedia/'
PRODUCTION_MEDIA_URL = '/media/'

GLOBAL_MEDIA_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)

