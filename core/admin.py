from django.contrib import admin
from .models import Product,CartItem,Checkout
from .models import HomePageImage
# Register your models here.
admin.site.register(HomePageImage)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'rating')
    search_fields = ('name', 'description')
    list_filter = ('price', 'rating')


@admin.register(CartItem)    
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'size', 'quantity', 'added_at')
    search_fields = ('user__username', 'product__name', 'size')
    list_filter = ('added_at',)


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'payment_method', 'order_date']
    list_filter = ['payment_method', 'order_date']
    search_fields = ['user__username', 'name', 'contact_number', 'address']
    



