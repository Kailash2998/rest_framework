from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm,CutomerProfileForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobile = Product.objects.filter(category='M')
        cart_count = Cart.objects.filter(user=request.user).count()
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobile':mobile,'cart_count':cart_count})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})
    
def add_to_cart(request):
    user=request.user
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    reg = Cart(user=user,product=product)
    reg.save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        #get the current login user and the show cart on the basis of the user id.
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 50
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        cart_count = Cart.objects.filter(user=request.user).count()
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * float(p.product.discounted_price))
                amount +=tempamount
                total_amount = amount+shipping_amount
            return render(request,'app/addtocart.html',{'carts':cart,'amount':amount,'total_amount':total_amount,'cart_count':cart_count})
        else:
            return render(request,"app/emptycart.html")


def plus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        print(product_id)
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 50
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
        for p in cart_product:
            tempamount = (p.quantity * float(p.product.discounted_price))
            amount +=tempamount
            total_amount = amount+shipping_amount
            data ={
                'quantity':c.quantity,
                'amount':amount,
                'total_amount' : total_amount 
            }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        print(product_id)
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 50
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
        for p in cart_product:
            tempamount = (p.quantity * float(p.product.discounted_price))
            amount +=tempamount
            total_amount = amount+shipping_amount
            data ={
                'quantity':c.quantity,
                'amount':amount,
                'total_amount' : total_amount 
            }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        print(product_id)
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 50
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
        for p in cart_product:
            tempamount = (p.quantity * float(p.product.discounted_price))
            amount +=tempamount
            total_amount = amount+shipping_amount
            data ={
                'amount':amount,
                'total_amount' : total_amount 
            }
        return JsonResponse(data)

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
    address = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'address':address,'active':'btn btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data == None:
        mobile = Product.objects.filter(category="M")
    elif data == 'iphone' or data == 'redmi':
        mobile = Product.objects.filter(category="M").filter(brand=data)
    return render(request, 'app/mobile.html',{'mobile':mobile})

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistration(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"congratulations !!! Registered Successfully")
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})

def checkout(request):
    user=request.user
    address= Customer.objects.filter(user=user)
    print(address)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 50
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
    if cart_product:
        for p in cart_product:
          tempamount = (p.quantity * float(p.product.discounted_price))
          amount +=tempamount
        total_amount = amount+shipping_amount
    return render(request, 'app/checkout.html',{'address':address,'total_amount':total_amount,'amount':amount,'cart_items':cart_items})

def payment_done(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    for c in cart:
        reg=OrderPlaced(user=user,product=c.product,quantity=c.quantity)
        reg.save()
        c.delete()
    return redirect("orders")

class ProfileView(View):
    def get(self, request):
        # Check if the user already has a profile
        user_profile, created = Customer.objects.get_or_create(user=request.user)
        
        # If the profile is newly created, initialize the form with empty data
        if created:
            form = CutomerProfileForm()
        else:
            # Populate the form with the user's profile data as initial data
            form = CutomerProfileForm(initial={
                'name': user_profile.name,
                'locality': user_profile.locality,
                'city': user_profile.city,
                'state': user_profile.state,
                'zipcode': user_profile.zipcode,
            })
            
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn btn-primary'})
    
    def post(self, request):
        form = CutomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            # Check if the user already has a profile
            user_profile, created = Customer.objects.get_or_create(user=usr)
            # Update the profile fields
            user_profile.name = name
            user_profile.locality = locality
            user_profile.city = city
            user_profile.state = state
            user_profile.zipcode = zipcode
            user_profile.save()
            
            messages.success(request, "Congratulations, profile updated successfully!")
        return render(request, 'app/profile.html', {'form': form}) 

            
            