from django.db import models

# Create your models here.
class Process(models.Model):
	step1 = models.TextField(max_length = 500)

class Collect(models.Model):
	grain = models.CharField(max_length = 90)
	date = models.DateField(max_length = 130)
	store = models.TextField(max_length = 500)
	fkey = models.ForeignKey(Process, on_delete = models.CASCADE)


