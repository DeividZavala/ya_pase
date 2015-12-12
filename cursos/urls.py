from django.conf.urls import include, url
from . import views

urlpatterns = [
     url(r'^$', views.GetCursosView.as_view(), name='get_cursos'),
     url(r'^cursos/(?P<id>\d+)',views.ShowCurso.as_view(),name='show_curso'),
     url(r'^curso/(?P<id>\d+)/(?P<id_clase>\d+)',views.ShowClase.as_view(),name='show_clase'),
     url(r'^pago/',views.Pagos.as_view(),name='pago'),
]