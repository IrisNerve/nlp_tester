from django.db import models

class Article(models.Model):
	text = models.TextField()

class Tag(models.Model):
	ALCHEMY = 0
	OPEN_CALAIS = 1
	SERVICES = (
		(ALCHEMY, 'Alchemy'),
		(OPEN_CALAIS, 'Open Calais'),
	)

	article = models.ForeignKey(Article)
	tag = models.TextField()
	service = models.IntegerField(choices = SERVICES)
	vote = models.BooleanField(default = False)