from django.db import models
from django.contrib.auth.models import User

# class category for category on product site
class Category(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name
    
# class product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=3)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
    
# class Order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produks = models.ManyToManyField(Product, through='OrderItem')
    total_harga = models.DecimalField(max_digits=10, decimal_places=3)
    tanggal_order = models.DateTimeField(auto_now_add=True)
    is_order = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id}"
    
# class order item for ordering some item
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    produk = models.ForeignKey(Product, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.produk.name} - {self.jumlah}"
    
