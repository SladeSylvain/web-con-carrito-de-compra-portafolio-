from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    # Obtener categorías para mostrar en la home si se requiere
    categories = Category.objects.all()
    return render(request, 'products/home.html', {'categories': categories})

def nosotros(request):
    return render(request, 'products/nosotros.html')

def presentacion(request):
    return render(request, 'products/presentacion.html')

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    
    # Determinar clase de color para el título basado en la categoría
    text_color = 'primary'
    if slug == 'microsoft':
        text_color = 'info'
    elif slug == 'mac':
        text_color = 'dark'
        
    context = {
        'category': category,
        'products': products,
        'text_color': text_color,
    }
    return render(request, 'products/category_detail.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
