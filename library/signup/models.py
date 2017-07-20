"""from django.db import models9

class register(models.Model):
	name=models.CharField(max_length=40,blank=True,null=False)
	email=models.EmailField(max_length=50,unique=True,null=False)
	password=models.CharField(max_length=28,blank=True,null=False)
	timestamp=models.DateTimeField(auto_now_add=True,)

# Create your models here.
"""
from django.db import models

class books(models.Model):
	author = models.CharField(max_length=40)
	title = models.CharField(max_length=50)
	specifications = models.FileField(null=True)
	total = models.PositiveSmallIntegerField(default=1)
	