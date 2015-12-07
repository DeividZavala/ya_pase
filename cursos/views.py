from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from .models import Curso,Tema

# Create your views here.


class GetCursosView(View):
	def get(self, request):
		template = 'cursos/index.html'
		cursos=Curso.objects.all()
		context={
		"cursos":cursos,
		}
		return render(request, template,context)

class ShowCurso(View):
	def get(self,request,id):
		template="cursos/curso.html"
		curso=get_object_or_404(Curso,pk=id)
		temas=Tema.objects.all()
		context={
		"curso":curso,
		"temas":temas,
		}
		return render(request,template,context)

		
class ShowClase(View):
	pass
	# def get(self,request,id,id_clase):