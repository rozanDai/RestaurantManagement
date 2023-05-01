from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm

from .models import Menu, SubCategory,Customer, OrderItem, Order
# Create your views here.

# def index(request:
    # menus = Menu.objects.all)
    # return render(request, "ForkAndKnife/index.html", {'menuss': menus)

# Define a view function to display the home page
def index(request):
    # Get all the Menu objects from the database
    menus = Menu.objects.all()
    
    # Render the index.html template with the menus as context
    return render(request, "ForkAndKnife/index.html", {'menuss': menus})

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('homePage')
        else:
            messages.error(request, 'Login failed. Please try again.')
            #error_message = 'Invalid username or password.'
            #return render(request, "ForkAndKnife/signin.html", {'error_message': error_message})
    #else:
     #   return render(request, 'ForkAndKnife/signin.html')
    return render(request, "ForkAndKnife/signin.html")

# def signup(request):
    # if request.method == 'POST':
        # form = CustomUserCreationForm(request.POST)
        # if form.is_valid():
            # form.save()
            # return redirect('loginPage')
    # else:
        # form = CustomUserCreationForm()
    # return render(request, 'ForkAndKnife/joinnow.html', {'form': form})
# 
    #return render(request, "ForkAndKnife/joinnow.html")

# Define a view function to handle user registration
def signup(request):
    
    # If the request method is POST, process the form data
    if request.method == 'POST':
        # Create a new instance of the CustomUserCreationForm using the form data
        form = CustomUserCreationForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the user to the database
            form.save()
            
            # Redirect to the login page
            return redirect('loginPage')
    
    # If the request method is not POST, display an empty form
    else:
        form = CustomUserCreationForm()
    
    # Render the joinnow.html template with the form
    return render(request, 'ForkAndKnife/joinnow.html', {'form': form}) 

#from .models import CustomUser

#def signup(request):

    
 #   return render(request, 'ForkAndKnife/joinnow.html',)


def logoutview(request):
    logout(request)
    return redirect('indexPage')

'''
#@login_required
def home(request):
    if request.user.is_authenticated:
        menus = Menu.objects.all()
        return render(request, 'ForkAndKnife/home.html',{'menuss': menus})
    else:
        return redirect('loginPage') '''

def home(request):
    menus = Menu.objects.all()
    return render(request, 'ForkAndKnife/home.html',{'menuss': menus})


def menu(request):
    return render(request, "ForkAndKnife/menu.html",)

def about(request):
    return render(request, 'ForkAndKnife/about.html')

# def profile(request,username):
    # user = get_object_or_404(User, username=username)
    # profile = get_object_or_404(User, user=user)
    # context = {'user': user, 'profile': profile}
    # return render(request, "ForkAndKnife/profile.html",context)

@login_required
def profile(request):
    user = request.user
    customer = Customer.objects.get(id=user.id)
    context = {
        'user': user,
        'customer': customer,
        'phone_number': customer.phone_number,
        'address': customer.address,        

    }

    return render(request, 'ForkAndKnife/profile.html',context)

def menuFoodList(request):
    obj = SubCategory.objects.all()
    menus = Menu.objects.all()

    return render(request, "ForkAndKnife/menuFood.html", {'objj': obj , 'menuss': menus})

def orderItem(request, id):
    order = get_object_or_404(Menu, id = id)

    if request.method == "POST":
        quantity = request.POST.get('quantity')
        user = request.user
        #order, created = Order.objects.get_or_create(user=request.user)
        order_item = OrderItem( quantity=quantity, item_id=order.id, user=user)
        order_item.save()
       # print(order_item.get_total)
       # order.items.add(order_item)
        #order.total += order_item.price
        #order.save()


        #order_item = OrderItem(prod= 'prod',quantity='quantity', id = 'idd',)
      #  order.save()
        #return HttpResponse(user)

        return redirect('menuPage')


    return render(request, "ForkAndKnife/orderMenu.html", { 'order': order})  





def menuDrinkList(request):
     obj = SubCategory.objects.all()
     menus = Menu.objects.all()
    
     return render(request, "ForkAndKnife/menuDrink.html", {'objj': obj , 'menuss': menus})


def menuBakeryList(request):
     obj = SubCategory.objects.all()
     menus = Menu.objects.all()
    
     return render(request, "ForkAndKnife/menuBakery.html", {'objj': obj , 'menuss': menus})


def menuDesertList(request):
     obj = SubCategory.objects.all()
     menus = Menu.objects.all()
    
     return render(request, "ForkAndKnife/menuDeserts.html", {'objj': obj , 'menuss': menus})

'''
#@ogin_required
def cart(request):
    cart_items = OrderItem.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
        'total_cost': sum(item.total_cost for item in cart_items)
    }
    #return render(request, 'cart.html', context)
    return HttpResponse("This is cart....!!!")


#@login_required
def add_to_cart(request, product_id):
    food = Menu.objects.get(id=product_id)
    cart_item, created = OrderItem.objects.get_or_create(
        user=request.user,
     #   foods=food,
        defaults={'quantity': 1, 'total_cost': food.price}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.total_cost += food.price
        cart_item.save()
    messages.success(request, 'Item added to cart.')
    return redirect('orderPage')
'''


#@login_required
def place_order(request):
    if request.method== 'POST':
        address = request.POST.get('address')
        #number = request.POST.get('number')
        cart_items = OrderItem.objects.filter(user=request.user)
        total_quantity = 0
        for i in cart_items:
            total_quantity += i.quantity
        total = total_quantity
        total_cost = sum(item.get_total for item in cart_items)
        order = Order.objects.create(user=request.user,delivery_address=address, quantity=total,
                                     total_price = total_cost )
#        order = Order(delivery_address=address, quantity=total,
 #                      total_price = total_cost )
       # order.items.set(cart_items)
        order.save()
        cart_items.delete()
        messages.success(request, 'Order placed successfully.')
        return redirect('homePage')

'''
#@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-date_created')
    context = {
        'orders': orders
    }
    return render(request, 'order_history.html', context) '''

# 
#@login_required
def cart(request):
    items = OrderItem.objects.filter(user=request.user)
   # total_price = sum(item.get_total() for item in items)
    #name = items.item_id.name
    #context = {'items': items}
   # return HttpResponse(items)
    total_price = 0
    for i in items:
        total_price += i.get_total
    total = total_price
        
    return render(request, 'ForkAndKnife/cart.html', {'context': items, 'total' : total })
# 
#@login_required
# def remove_from_cart(request, item_id):
    # Cart.objects.filter(user=request.user, item_id=item_id).delete()
    # messages.success(request, "Item removed from cart.")
    # return redirect('cart')

# 
# from .forms import CartItemForm
# 
# def update_cart(request,):
    # 
    # item = OrderItem.objects.all()
    # if request.method == 'POST':
        # form = CartItemForm(request.POST, instance=item)
        # if form.is_valid():
            # form.save()
            # return redirect('cartPage')
    # else:
        # form = CartItemForm(instance=item)
    # return render(request, 'updateCart.html', {'form': form})
# 

def update_cart(request, id):
    # get the item id and new quantity from the POST data
    id = str(id)
    quantity = int(request.POST['quantity'])
   # update the item quantity in the cart
    cart_item = OrderItem.objects.filter(id=id).first()
    print(f"quantiy is : {cart_item}")
    try:
        cart_item = OrderItem.objects.get(id=id)
    except OrderItem.DoesNotExist:
        print(f"No OrderItem found with item_id={id}")

    if cart_item is not None:
        #cart_item.quantity = quantity
        #cart_item.save()
        cart_item.quantity = quantity
        print(f"Quantity updated to {quantity}")
        cart_item.save()
        print("Item saved to database")


    return redirect('cartPage')



def delete_cart(request, id):
    # Get the item id
    item_id = int(id)
    
    # Get the order item to be deleted
    order_item = OrderItem.objects.get(id=item_id)
    
    # Delete the order item from the cart
    order_item.delete()
    
    # Redirect to the cart page
    return redirect('cartPage')


@login_required

def delete_account(request):
    if request.method == 'POST':
        # Delete the user's data
        request.user.delete()
        # Log the user out
        logout(request)
        messages.success(request, 'Your account has been deleted.')
        return redirect('indexPage')
    return render(request, 'ForkAndKnife/deleteUser.html')