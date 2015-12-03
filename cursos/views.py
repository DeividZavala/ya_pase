from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class GetCursosView(View):
	def get(self, request):
		template = 'cursos/index.html'
		return render(request, template)