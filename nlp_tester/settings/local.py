from nlp_tester.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'Ego371!FTW',
        'NAME': 'nlp_tester',
    }
}

INSTALLED_APPS += (
	'debug_toolbar',
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True