from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('produk/<int:produk_id>/', views.produk_detail, name='produk_detail'),
    path('tambah_keranjang/<int:produk_id>/', views.tambah_keranjang, name='tambah_keranjang'),
    path('lihat_keranjang/', views.lihat_keranjang, name='lihat_keranjang'),
    path('checkout/', views.checkout, name='checkout'),
]