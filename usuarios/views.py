from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .forms import RegistroUserForm
from django.views.generic import View
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Permission,User
from django.contrib.contenttypes.models import ContentType


# content_type=ContentType.objects.get_for_model(User)
# permission=Permission.objects.create(codename="econo1",name="Ver curso de ecnonomia 1",content_type=content_type)
def user_gain_perms(request,user_id):
	user=get_object_or_404(User,pk=user_id)
	permission=Permission.objects.get(codename="econo1")
	user.user_permissions.add(permission)
	user.has_perm("usuarios.econo1")
	user=get_object_or_404(User,pk=user_id)
	user.has_perm("usuarios.econo1")

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

			permission = Permission.objects.get(codename='econo1')
			user=User.objects.get(email=email)
			# user.groups.add(permission)
			user.user_permissions.add(permission)
			user.save()
			
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


class IndexView(View):
	# @login_required
	@method_decorator(login_required)
	def get(self,request):
		template="usuarios/index.html"
		return render(request,template)

class LoginView(View):
	def get(self,request):
		template="usuarios/login.html"
		if request.user.is_authenticated():
			return redirect(reverse("show_index"))
		else:
			mensaje=""
			return render(request,template)

	def post(self,request):
		template="usuarios/login.html"
		username=request.POST.get("username","")
		password=request.POST.get("password","")
		user=authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect(reverse("show_index"))
			else:
				mensaje="La cuenta no está activa"
				context={
				"mensaje":mensaje,
				}
				return render(request,template,context)
		else:
			mensaje="Nombre de usuario o contraseña no valido"
			context={
			"mensaje":mensaje,
			}
			return render(request,template,context)

class LogoutView(View):
	def get(self,request):
		logout(request)
		messages.success(request,"Te has desconectado con éxito.")
		return redirect(reverse('get_cursos'))