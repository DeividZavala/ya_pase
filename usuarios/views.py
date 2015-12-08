from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .forms import RegistroUserForm
from django.views.generic import View
from .models import UserProfile


# Create your views here.

class Registro(View):
	def get(self,request):
		template="usuarios/registro.html"
		form=RegistroUserForm()
		context={
		"form":form
		}
		return render(request,template,context)

	def post(self,request):
		template="usuarios/registro.html"
		form=RegistroUserForm(request.POST,request.FILES)
		
		if form.is_valid():
			cleaned_data=form.cleaned_data
			username=cleaned_data.get("username")
			password=cleaned_data.get("password")
			email=cleaned_data.get("email")
			photo=cleaned_data.get("photo")
			user_model=User.objects.create_user(username=username,password=password)
			user_model.email=email
			user_model.save()
			user_profile=UserProfile()
			user_profile.user=user_model
			user_profile.photo=photo
			user_profile.save()
			return redirect(reverse('show_gracias', kwargs={'username': username}))
		else:
			context={
			"form":form
			}
			return render(request,template,context)


class GraciasView(View):
	def get(self,request,username):
		template="usuarios/gracias.html"
		context={
		"username":username,
		}
		return render(request,template,context)
