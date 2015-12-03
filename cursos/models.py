from __future__ import unicode_literals
from django.db import models

class Curso(models.Model):
	titulo=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=150)
	masinfo=models.TextField()
	img=models.URLField()
	video_link=models.URLField()
	author=models.ForeignKey('auth.User')

	def __str__(self):
		return self.titulo
