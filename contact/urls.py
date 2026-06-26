from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto, name='contacto'),
    path('borrar/<int:pk>/', views.borrar_contacto, name='borrar_contacto'),
]
