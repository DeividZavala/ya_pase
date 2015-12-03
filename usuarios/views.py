from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class GetUsuariosView(View):
	def get(self, request):
		
		template = 'usuarios/index.html'
		

		
		# return HttpResponse(dinosaur)
		return render(request, template)