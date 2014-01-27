from django.shortcuts import render
from django.http import HttpResponse

from nlp_tester.models import *

# Page loaders
def index(request):
	return render(request, "index.html")

# POST Responses
def analyze_url(request):
	from goose import Goose
	url = request.POST['url']
	g = Goose()
	article = g.extract(url=url)
	return HttpResponse(article.cleaned_text)