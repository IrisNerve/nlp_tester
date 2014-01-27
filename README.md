Iris NLP Tester
==========

Installation
------------
	mkvirtualenv nlp_tester
	git clone https://github.com/IrisNerve/nlp_tester.git
	cd nlp_tester
	pip install -r requirements.txt
	python manage.py syncdb

Test
----

Run the command
	
	python manage.py runserver

Go to 127.0.0.1:8000 in a browser. 
Enter the URL of the article you want to analyze and hit "Analyze!"