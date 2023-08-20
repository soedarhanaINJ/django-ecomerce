from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem

def produk_list(request):
    produks = Product.objects.all()

    return render(request, 'produklist.html', {'produks': produks})

def produk_detail(request):
    produk = get_object_or_404(Product, pk=produk_id)

    return render(request, 'produkdetail.html', {'produk': produk})

# login account need for add item to chart
@login_required
def tambah_keranjang(request):
    produk = get_object_or_404(Product, pk=produk_id)
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, produk=produk)
    order_item.jumlah += 1
    order_item.save()

    return redirect('produk_list')

# login account need for view the chart
@login_required
def lihat_keranjang(request):
    order = Order.objects.get(user=request.user, is_order=False)
    order_items = order.orderitem_set.all()
    
    return render(request, 'template/lihatkeranjang.html', {'order': order, 'order_items': order_items})

# login account need for checkout the item
@login_required
def checkout(request):
    order = Order.objects.get(user=request.user, is_order=False)
    order.is_ordered = True
    order.save()

    return render(request, 'template/checkout.html', {'order': order})

