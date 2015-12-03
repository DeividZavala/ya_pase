from django.conf.urls import include, url

from . import views

urlpatterns = [
     url(r'^$', views.GetUsuariosView.as_view(), name='get_usuario'),
]
