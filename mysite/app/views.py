from django.shortcuts import render,redirect
from django.http  import HttpResponse
from.models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'app/register.html',context={'form':form})
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Sai !Bạn vui lòng kiểm tra tài khoản và mật khẩu !')
    context = {}
    return render(request,'app/login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('login')
def home(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    Products = Product.objects.all()
    return render(request,'app/home.html',context= {'products' : Products,'user_not_login':user_not_login,'user_login':user_login})
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context= {'items' : items,'order': order}
    return render(request,'app/cart.html',context)
def checkout(request):
    return render(request,'app/checkout.html',context={})
def buttun(request):
    Video18s = Video18.objects.all()
    return render(request,'app/buttun.html',context={'Video18s' : Video18s})
def video18(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    Video18s = Video18.objects.all()
    return render(request,'app/video18.html',context={'Video18s' : Video18s,'user_not_login':user_not_login,'user_login':user_login})
def diemdanh(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    
    money_items = money_item.objects.all()
    return render(request,'app/diemdanh.html',context={'money_items': money_items,'user_not_login':user_not_login,'user_login':user_login})

