# from django.shortcuts import render
# from django.views.generic import View
# from django.shortcuts import get_object_or_404 ,redirect
# from django.http import HttpResponse
# from models import Usuario


# # Create your views here.

# class GetUsuariosView(View):
# 	def get(self, request):
		
# 		template = 'usuarios/index.html'
		

		
# 		# return HttpResponse(dinosaur)
# 		return render(request, template)

# class NuevoUsuario(View):
# 	def get(self, request):
# 		template = 'usuarios/login.html'
# 		return render (request, template)

# 	def post(self, request):
# 		username = self.request.POST.get('nombre','')
# 		email = self.request.POST.get('email', '')
# 		password = self.request.POST.get('pass1','')

# 		user = Usuario(
# 			username = self.username,
# 			email = self.email,
# 			password = self.password,
# 		)

# 		user.save()

# 		return redirect('/usuarios')