from django.shortcuts import render,redirect
from django.contrib.auth.forms import authenticate
from . models import *
from . forms import Signup
from django.http import JsonResponse
import json
import smtplib
from django.core import mail

my_list=[]
check = True
username=''
def login(request):
    global username
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = Customer.objects.filter(user=username,password=password)
        print(username)

        if customer:
            print('done')
            return redirect('index')
        else:
            print('Fails')

    return render(request, 'login.html')

def index(request):

    stok = stock.objects.all()
    return render(request,'index.html',{'stok':stok})

def signup_view(request):

    return render(request,'signup.html')


def signup(request):

    if request.method == "POST":
        customer = Customer()
        customer.user = request.POST.get('username')
        customer.email = request.POST.get('emailid')
        customer.password = request.POST.get('password')
        customer.save()
        return redirect("login")


    return render(request,"signup.html")

def search(request):

    if request.method =='POST':
        print('in search')
        proname= request.POST.get('search')
        print(proname)
        stok = stock.objects.filter(pname=proname)
        return render(request, 'index.html', {'stok': stok})




def login_view(request):
    return render(request,'login.html')


def updateitem(request):
    global username, my_list
    global check
    customer = Customer.objects.filter(user=username)
    print(customer[:], type(customer))
    data = json.loads(request.body)
    productId = data['productId']
    action =  data['action']
    product= stock.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer[0],complete=False)

    orderitem,created = OrderItem.objects.get_or_create(order = order,product=product)
    if action=="add":
        orderitem.quantity = (orderitem.quantity + 1)
        if ((product.quan>= orderitem.quantity) ):
            my_list.append(True)
            print(check)
        else:
            my_list.append(False)

        print(my_list)


    elif action=="remove":
        my_list.clear()
        orderitem.quantity = (orderitem.quantity - 1)
        if (product.quan>= orderitem.quantity):
            my_list.append(True)
            print(my_list)
        else:
            my_list.append(False)
            print(my_list)


    orderitem.save()
    print('action: ', action)
    print('action: ', productId)
    return JsonResponse("item was added", safe=False)


def cart(request):
    global username
    # customer = Customer.objects.get(user=username)
    customer  = Customer.objects.filter(user=username)

    order, created = Order.objects.get_or_create(customer=customer[0],complete=False)
    items = order.orderitem_set.all()
    i=1
    context = {'items':items,'order':order ,'i':i}
    return render(request,'cart.html',context)

def email(request):
    global my_list
    customer = Customer.objects.filter(user=username)
    print(customer[0])
    email_to = str(customer[0])
    if request.method =="POST":
        mail= smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.login('pallavparikh98@gmail.com','pallav98')

        # for i in range(len(my_list)):
        if not any(my_list):
               message = 'Order is not placed due to lack of stock'
               mail.sendmail('pallavparikh98@gmail.com',email_to,message)
               my_list.clear()
               mail.quit()

               return redirect('carts')
        else:
               message= "Order placed Successfully "
               mail.sendmail('pallavparikh98@gmail.com',email_to,message)
               mail.quit()
               my_list.clear()
               print(my_list)
               return redirect('index')
