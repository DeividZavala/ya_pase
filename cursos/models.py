from __future__ import unicode_literals
from django.db import models

class Curso(models.Model):
	titulo=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=150,blank=True)
	masinfo=models.TextField()
	img=models.URLField()
	video_link=models.URLField()
	author=models.ForeignKey('auth.User')
	temas=models.ManyToManyField('Tema',blank=True)

	def __str__(self):
		return self.titulo

class Tema(models.Model):
	titulo=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=150,blank=True)
	numero=models.FloatField()
	subtemas=models.ManyToManyField('Clase',blank=True)
	# curso_padre=models.ForeignKey('Curso')

	def __str__(self):
		return self.titulo

class Clase(models.Model):
	titulo=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=150,blank=True)
	numero=models.FloatField()
	Vide_link=models.URLField()
	# curso_padre=models.ManyToManyField('Curso')
	# subtema_padre=models.ForeignKey('Tema')



	def __str__(self):
		return self.titulo
