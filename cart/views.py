from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Cart, CartItem

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        
        # Obtener cantidad del formulario
        try:
            quantity = int(request.POST.get('quantity', 1))
        except ValueError:
            quantity = 1
            
        if quantity < 1:
            quantity = 1
            
        if product.stock < quantity:
            messages.error(request, f'No hay suficiente stock disponible de {product.name}.')
            return redirect('product_detail', pk=product_id)
            
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        if not item_created:
            new_qty = cart_item.quantity + quantity
            if product.stock < new_qty:
                messages.warning(request, f'No puedes agregar más de {product.stock} unidades de este producto.')
                return redirect('cart_detail')
            cart_item.quantity = new_qty
        else:
            cart_item.quantity = quantity
            
        cart_item.save()
        messages.success(request, f'¡{product.name} añadido al carrito!')
        return redirect('cart_detail')
        
    return redirect('home')

@login_required
def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        product_name = cart_item.product.name
        cart_item.delete()
        messages.warning(request, f'¡{product_name} eliminado del carrito!')
    return redirect('cart_detail')

@login_required
def update_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity >= 1:
                if cart_item.product.stock < quantity:
                    messages.warning(request, f'Solo hay {cart_item.product.stock} unidades disponibles de {cart_item.product.name}.')
                else:
                    cart_item.quantity = quantity
                    cart_item.save()
                    messages.info(request, f'Cantidad de {cart_item.product.name} actualizada.')
            else:
                cart_item.delete()
                messages.warning(request, f'¡{cart_item.product.name} eliminado del carrito!')
        except ValueError:
            pass
    return redirect('cart_detail')
