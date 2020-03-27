from django.db import models

# Create your models here.
class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

	#if we don't write this function then every item in the list will be shown as object in the database
	def __str__(self):
		return self.item + ' | ' + str(self.completed)