from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.conf import settings

from article_analyze.models import *

from goose import Goose
from calais import Calais
from operator import itemgetter

'''
	Page loaders
'''

# Load the index page
# Users can input an article URL here.
def index(request):
	return render(request, "index.html")

'''
	POST Responses
'''

# Extract article text and analyze
def analyze_url(request):
	# Insert the article into the database
	a = Article(
		url = request.POST['url']
	)
	a.save()

	# Use Goose to get the article text
	g = Goose()
	article_text = g.extract(url = a.url).cleaned_text.encode('utf-8')

	# Use python-calais to analyze the article text
	calais = Calais(settings.OC_API_KEY)
	result = calais.analyze(article_text)

	result.print_summary()

	# List of tags for UI
	tag_list = []
	
	try:
		# Create a dictionary to store all the entities and relevance scores
		# Get rid of all duplicates
		entity_dict = dict([])
		for entity in result.entities:
			if not entity_dict.has_key(entity['name']):
				entity_dict[entity['name']] = entity['relevance']	

		# Sort the entities and topics by confidence/relavence
		entity_list = sorted(entity_dict.iteritems(), key=itemgetter(1), reverse=True)

		# Insert the OpenCalais entities and topics with confidence > .3 into the database and add to a list for UI
		for tag, confidence in entity_list:
			if confidence > .3:
				t = Tag(
					article = a,
					tag = tag,
					confidence = confidence,
					service = Tag.OPEN_CALAIS,
				)
				t.save()
				tag_list.append(t)
			else:
				break
	except KeyError:
		print 'No entities found'

	try:
		# Create a dictionary to store all the topics and relevance scores
		# Get rid of all duplicates
		topic_dict = dict()
		for topic in result.simplified_response['topics']:
			if not topic_dict.has_key(topic['categoryName']):
				topic_dict[topic['categoryName']] = topic['score']

		# Sort topics by relavence
		topic_list = sorted(topic_dict.iteritems(), key=itemgetter(1), reverse=True)

		for tag, confidence in topic_list:
			if confidence > .3:
				t = Tag(
					article = a,
					tag = tag,
					confidence = confidence,
					service = Tag.OPEN_CALAIS,
				)
				t.save()
				tag_list.append(t)
			else:
				break
	except KeyError:
		print 'No topics found'

	# Context for the template
	c = {
		'tags': tag_list
	}

	return render(request, 'tag_list.html', c)