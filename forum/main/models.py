from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	text = models.TextField()
	author = models.ForeignKey(User, default=None)
	date = models.DateTimeField()

	def __str__(self):
		return self.text
