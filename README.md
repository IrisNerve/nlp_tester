Iris NLP Tester
==========

Installation
------------
Make sure you have virtialenv and virtualenvwrapper installed. Look [here](http://virtualenvwrapper.readthedocs.org/en/latest/) for instructions in case you don't.

	mkvirtualenv nlp_tester
	git clone https://github.com/IrisNerve/nlp_tester.git

At this point, you should open up nlp_tester/settings/local.py and change the values to your own local values. My file (local.py) looks like

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
	TEMPLATE_DEBUG = True.

Continue with the installation when you have that
	
	cd nlp_tester
	pip install -r requirements.txt
	python manage.py syncdb --settings=nlp_tester.settings.local
	python manage.py migrate article_analyze --settings=nlp_tester.settings.local

Test
----

Run the command
	
	python manage.py runserver --settings=nlp_tester.settings.local

Go to [127.0.0.1:8000](http://127.0.0.1:8000) in a browser. 

Enter the URL of the article you want to analyze and hit "Analyze!"

Known Issues
------------

Right now, although the process runs, there is no indication in the UI. I'm having a hard time constructing the list of tags to show in the UI. If someone can figure this out (Shawn pls), please fix it.