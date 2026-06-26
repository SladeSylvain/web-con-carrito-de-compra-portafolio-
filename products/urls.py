from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('presentacion/', views.presentacion, name='presentacion'),
    # Compatibilidad con las rutas originales usando parámetros extra
    path('productos1/', views.category_detail, {'slug': 'linux'}, name='productos1'),
    path('productos2/', views.category_detail, {'slug': 'microsoft'}, name='productos2'),
    path('productos3/', views.category_detail, {'slug': 'mac'}, name='productos3'),
    path('categoria/<slug:slug>/', views.category_detail, name='category_detail'),
    path('producto/<int:pk>/', views.product_detail, name='product_detail'),
]
