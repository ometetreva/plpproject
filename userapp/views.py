from django.shortcuts import render, redirect, HttpResponse
from .models import User, Product, Order

# Create your views here.

def signup(request):
    return render(request, 'register.html')

def process_form(request):
    if request.method == 'POST':
        First_Name = request.POST.get('First Name')
        Last_Name = request.POST.get('Last Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')

        if First_Name and Last_Name and Email and Password:
            user = User(First_Name=First_Name, Last_Name=Last_Name, Email=Email, Password=Password)
            user.save()
            message = 'Account created successfully'
            return render(request, 'redirect.html', {'message': message, 'login': True})
        else:
            message = 'Error creating account'
            return render(request, 'redirect.html', {'message': message, 'login': False})
    else:
        return redirect('signup')
    
def login(request):
    if request.session.get('name'):
        return render(request, 'home.html', {'name': request.session['name']})
        
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')

        try:
            user = User.objects.get(Email=Email)
            # First_Name = user.First_Name
            User_ID = user.id
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
        
        if Password == user.Password:
            # request.session['name'] = First_Name
            request.session['user_id'] = User_ID
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    else: 
        return render(request, 'login.html')

def home(request):
    mens_fashion = Product.objects.filter(Main_Category='Men', Sub_Category='Clothing')
    ladies_fashion = Product.objects.filter(Main_Category='Ladies', Sub_Category='Clothing')
    product_categories = {
        'mens_fashion': mens_fashion,
        'ladies_fashion': ladies_fashion
    }
    return render(request, 'home.html', {'Product_Categories': product_categories})

def logout(request):
    if request.session['user_id']:
        del request.session['user_id']
        return redirect('login')
    else:
        return redirect('login')
    
def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product_details': product})

def add_to_cart(request, id):
    if not(Order.objects.filter(Customer_ID=request.session['user_id'], Product_ID=id, Order_Status='Pending')):
        order = Order(Customer_ID=request.session['user_id'], Product_ID=id)
        order.save()

    return redirect('cart')

def cart(request):
    orders = Order.objects.filter(Customer_ID=request.session['user_id'])
    products_details = [
        {
            'product': Product.objects.get(id=order.Product_ID),
            'quantity': order.Product_Quantity,
            'order_ID': order.id
        } for order in orders
    ]
    return render(request, 'cart.html', {'products_details': products_details})

def decrease_quantity(request, id):
    order = Order.objects.get(id=id)

    if order.Product_Quantity > 1:
        order.Product_Quantity -= 1
        order.save()

    return redirect('cart')

def increase_quantity(request, id):
    order = Order.objects.get(id=id)
    order.Product_Quantity += 1
    order.save()

    return redirect('cart')

def remove(request, id):
    Order.objects.get(id=id).delete()
    return redirect('cart')