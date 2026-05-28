
from django.contrib import admin
from django.urls import path, include
from myfirstapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('perfil/', views.perfil, name='perfil'),
    path('tareas/', views.tareas, name='tareas'),
    path('productos1/', views.productos1, name='productos1'),
    path('productos2/', views.productos2, name='productos2'),
    path('productos3/', views.productos3, name='productos3'),
    path('presentacion/', views.presentacion, name='presentacion'),
    path('registro/', views.registro, name='registro'),
    path('admin', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contacto/borrar/<int:pk>/', views.borrar_contacto, name='borrar_contacto')
]