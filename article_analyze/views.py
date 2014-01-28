from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.conf import settings

from article_analyze.models import *

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
	# Use python-calais to analyze the article given by url
	calais = Calais(settings.OC_API_KEY)
	result = calais.analyze_url(request.POST['url'])

	# Create a dictionary to store all the tags and confidences
	# Get rid of all duplicates
	entity_dict = dict([])
	for entity in result.entities:
		if not entity_dict.has_key(entity['name']):
			entity_dict[entity['name']] = entity['relevance']

	# Sort the tags by confidence/relavence
	entity_list = sorted(entity_dict.iteritems(), key=itemgetter(1), reverse=True)

	# Insert the article into the database
	a = Article(
		url = request.POST['url']
	)
	a.save()

	# Insert the OpenCalais tags with confidence > .3 into the database
	for tag, confidence in entity_list:
		if confidence > .3:
			t = Tag(
				article = a,
				tag = tag,
				confidence = confidence,
				service = Tag.OPEN_CALAIS,
			)
			t.save()
		else:
			break

	c = {
		'entity_list': entity_list
	}
	return render(request, 'tag_list.html', c)