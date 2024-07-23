from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class HomePageImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='homepage_images/', blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Image"
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    

    def __str__(self):
        return self.name


class TrackingOrder(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='TrackingOrderItem', related_name='tracking_orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    tracking_number = models.CharField(max_length=50, blank=True, null=True)
    tracking_url = models.URLField(blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tracking Order #{self.id} by {self.user.username}"
    
    
class TrackingOrderItem(models.Model):
    order = models.ForeignKey(TrackingOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


#Tables for selection of size and quantity
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=[
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ])
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.product.name} ({self.size}) x {self.quantity}"
    
    
class Checkout(models.Model):
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('online', 'Online Payment'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    order_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Order for {self.user.username} on {self.order_date}"
    

    
    







    


