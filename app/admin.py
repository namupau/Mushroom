from django.contrib import admin
from .models import Cart,Customer,Product
from .models import UploadedImage


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'stock', 'available', 'category', 'product_image']
    list_filter = ['available', 'created', 'updated', 'category']
    search_fields = ['name', 'category']
    list_editable = ['price', 'stock', 'available']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'locality', 'city', 'state', 'phone','email']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product', 'quantity', 'total_cost']


@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'uploaded_at']