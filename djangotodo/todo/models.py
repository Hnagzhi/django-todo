from django.db import models
from django.conf import settings


class ToDoItem(models.Model):
	title = models.CharField(max_length=100)
	created_date = models.DateField()
	end_date = models.DateField()
	person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	description = models.CharField(max_length=1000)

