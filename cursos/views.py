from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.shortcuts import get_object_or_404, redirect
from .models import Curso,Tema,Clase
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

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
		temas=Tema.objects.all().order_by('numero')
		context={
		"curso":curso,
		"temas":temas,
		}
		return render(request,template,context)

		
class ShowClase(View):
	@method_decorator(permission_required("auth.econo1"),)
	# @permission_required("econo1")
	def get(self,request,id,id_clase):
		template="cursos/clase.html"
		curso=get_object_or_404(Curso,pk=id)
		# clase=get_object_or_404(Clase,pk=id_clase)
		clases_lista=Clase.objects.filter(curso_padre=id).order_by('numero')
		paginator = Paginator(clases_lista, 1)
		# page = request.GET.get(id_clase)
		page=id_clase
		try:
			clases = paginator.page(page)
		except PageNotAnInteger:
			clases=paginator.page(1)
		except EmptyPage:
			clases=paginator.page(paginator.num_pages)

		context={
		"curso":curso,
		# "clase":clase,
		"clases":clases,
		}
		return render(request,template,context)


class Pagos(View):
	# template_name = "cursos/pago.html"
	def get(self,request):
		template="cursos/pago.html"
		return render(request, template,)
