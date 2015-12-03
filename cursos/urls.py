from django.conf.urls import include, url

from . import views

urlpatterns = [
     url(r'^$', views.GetCursosView.as_view(), name='get_cursos'),
]