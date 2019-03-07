from django.db import models
from datetime import datetime

class information(models.Model):
	title = models.CharField(max_length=30)
	location = models.CharField(max_length= 40)

	def __str__(self):
		return self.title
