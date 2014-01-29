from django.db import models

class Article(models.Model):
	url = models.URLField()

class Tag(models.Model):
	ALCHEMY = 0
	OPEN_CALAIS = 1
	SERVICES = (
		(ALCHEMY, 'Alchemy'),
		(OPEN_CALAIS, 'Open Calais'),
	)

	article = models.ForeignKey(Article)
	tag = models.TextField()
	confidence = models.DecimalField(max_digits=5, decimal_places = 4, default=0)
	service = models.IntegerField(choices = SERVICES)
	vote = models.IntegerField(default = 0)

	def upvote(self):
		self.vote += 1
		self.save()