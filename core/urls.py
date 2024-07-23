from django.urls import path
from .views import home , add_to_cart,cart,register,login_view,register,contact_view,logout_view,track_order
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contact/', contact_view, name='contact_view'),
    path('track-order/', track_order, name='track_order'),


]