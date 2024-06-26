from django.shortcuts import render,redirect,get_object_or_404
from .models import HomePageImage
from .models import Product,CartItem,Checkout
from django.contrib.auth.decorators import login_required
from .forms import CartItemForm
from django.contrib import messages
from .forms import CheckoutForm
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.



def home(request):
    homepage_images = HomePageImage.objects.all()
    products = Product.objects.all()
    form = CartItemForm()
    return render(request, 'index.html', {'homepage_images': homepage_images, 'products': products, 'form': form})



#your view to handle the form submission and save the data to the database.
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        size = request.POST.get('size')
        quantity = request.POST.get('quantity')
        product = Product.objects.get(id=product_id)
        cart_item = CartItem.objects.create(
            user=request.user,
            product=product,
            size=size,
            quantity=quantity
        )
        
        return redirect('cart')
    return redirect('index')



def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_subtotal = sum(item.product.price * item.quantity for item in cart_items)
    delivery_fee = 150
    cart_total = cart_subtotal + delivery_fee
    
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'cart_subtotal': cart_subtotal,
        'delivery_fee': delivery_fee,
        'cart_total': cart_total,
    })


def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user).first() 
    print(f"Cart item: {cart_items}")# Example query to get the first item in the cart
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Save checkout details
            checkout_info = form.save(commit=False)
            checkout_info.user = request.user
            checkout_info.save()

            # Clear cart items after checkout
            cart_items.delete()

            return redirect('checkout_success')  # Redirect to a success page
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {
        'form': form,
        'cart_items': cart_items,
    })

def checkout_success(request):
    return render(request,'checkout_success.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Hello ! {username}.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message from {name}',
                message,
                email,
                ['asimalipeerzada@gmail.com'],  # Replace with your admin email
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})