from django.conf.urls import include, url

from . import views

urlpatterns = [
     url(
     	r'^registro/$',
     	views.Registro.as_view(),
     	name='show_registro'),
     url(
     	r'gracias/(?P<username>[\w]+)/$',
     	views.GraciasView.as_view(),
     	name='show_gracias'),
     url(
     	r'^$',
     	views.IndexView.as_view(),
     	name='show_index'),
     url(
     	r'^login/$',
     	views.LoginView.as_view(),
     	name="show_login"),
     url(
          r'^logout/$',
          views.LogoutView.as_view(),
          name="show_logout"),
]

