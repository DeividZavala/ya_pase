from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class UserProfile(models.Model):

	user=models.OneToOneField(settings.AUTH_USER_MODEL)
	photo=models.ImageField(upload_to='perfiles',blank=True,null=True)

	def __str__(self):
		return self.user.username