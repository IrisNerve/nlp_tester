from django.shortcuts import render
from django.http import HttpResponse

from nlp_tester.models import *
from nlp_tester.settings import OC_API_KEY

from calais import Calais
import json

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
	calais = Calais(OC_API_KEY)
	result = calais.analyze_url(request.POST['url'])
	#result = calais.analyze("George Bush was the President of the United States of America until 2009.  Barack Obama is the new President of the United States now.")
	for entity in result.entities:
		print entity['name'] + ' - ' + str(entity['relevance'])
	return HttpResponse(json.dumps(result.entities, indent=4))