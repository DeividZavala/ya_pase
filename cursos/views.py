from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from .models import Curso

# Create your views here.


class GetCursosView(View):
	def get(self, request):
		template = 'cursos/index.html'
		cursos=Curso.objects.all()
		context={
		"cursos":cursos,
		}
		return render(request, template,context)