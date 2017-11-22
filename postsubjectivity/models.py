# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class TextPost(models.Model):
	title = models.CharField(max_length=500)
	t = models.TextField()

class ImagePost(models.Model):
	embedding = models.CharField(max_length=5000, default="")

@python_2_unicode_compatible
class Alias(models.Model):
	name=models.CharField(max_length=200)
	date=models.DateTimeField('date created')
	logins=models.IntegerField()
	last_login=models.DateTimeField('last log')

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Habla(models.Model):
	text=models.CharField(max_length=600)
	date=models.DateTimeField('date published')
	alias=models.ForeignKey(Alias)

	def __str__(self):
		return self.text

class Beat(models.Model):
	tag=models.DateTimeField('tag')
	alias=models.ForeignKey(Alias)



