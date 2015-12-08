from django import forms 
from django.contrib.auth.models import User 

class RegistroUserForm(forms.Form):

	username=forms.CharField(
		min_length=5,
		widget=forms.TextInput(attrs={"class":"input-field"}))
	email=forms.EmailField(
		widget=forms.EmailInput(attrs={"class":"input-field"}))
	password=forms.CharField(min_length=1,
		widget=forms.PasswordInput(attrs={"class":"input-field"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"input-field"}))
	photo=forms.ImageField(required=False)

	def clean_username(self):
		"""Comprueba que no exista un username igual en la bd"""
		username=self.cleaned_data["username"]
		if User.objects.filter(username=username):
			raise forms.ValidationError("Nombre de usuario ya resgistrado.")
		return username

	def clean_email(self):
		"""Comprueba que no exista un email igual en la bd"""
		email=self.cleaned_data["email"]
		if User.objects.filter(email=email):
			raise forms.ValidationError("Este email ya se registro, use otro")
		return email

	def clean_password2(self):
		"""Comprueba que password y password2 coincidan"""
		password=self.cleaned_data["password"]
		password2=self.cleaned_data["password2"]
		if password != password2:
			raise forms.ValidationError("Las contraseña no coincide.")
		return password2
		