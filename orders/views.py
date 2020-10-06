from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import menu, toppings,order
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    all_table=menu.objects.values_list('dish', flat=True)
    name=[]
    for a in all_table:
        if a not in name:
            name.append(a)
        pass
    context = {
        "name":name,
        "menu": menu.objects.all()

    }
    return render(request, "orders/main.html", context)
    

def register(request):
    if request.method=="GET":
        return render(request, 'orders/signup.html')

    if request.method=="POST":
        try:
            user = User.objects.create_user(request.POST["username"])
            user.password=request.POST["password"]
            user.email=request.POST["email"]
            user.first_name=request.POST["firstname"]
            user.last_name=request.POST["lastname"]
            user.save()
            return redirect('index');
            
        except:
            error="Nickname already exist or has no value, check your data"
            return render(request, 'orders/error.html', {"error":error}) 
        
def logggin(request):
    if request.method=="GET":
        return render(request, 'orders/login.html')
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/error.html", {"error": "Incorrect username or password"})

def logout_view(request):
    logout(request)
    return redirect('index')


def makeorder(request):
    if request.method == 'POST':
        price=0
        #option_rows = request.POST.get('row')
        #id_dish=next(item for item in option_rows if item["name"] == "id")
        #amount=next(item for item in option_rows if item["name"] == "amount")
        #size=next(item for item in option_rows if item["name"] == "size")
        menu_var=menu.objects.get(id=request.POST["id"])
        quantity=int(request.POST["amount"])
        if request.POST['size'] == "small" or request.POST['size']=="standart":
            price+=menu_var.cost_small
        else:
            price+=menu_var.cost_large
        o=order(status="marked", menu=menu_var, amount=quantity, size=request.POST["size"])
        o.save()
        o.user=request.user
        #taking every add from user and add it to orders
        b=request.POST["adds"]
        a=json.loads(b)
        for add in a:
            print(add)
            menu_add=toppings.objects.get(topping=add)
            price+=menu_add.cost
            o.topping.add(menu_add)
        price=price*quantity
        o.price=price
        o.save()
    return HttpResponse("load")

def add_form(request):
    if request.method == 'POST':
        topp_list=[]
        pk=request.POST["id"]
        id_dish=menu.objects.get(id=pk)
        toppings=id_dish.toppingsss.all()
        size=id_dish.size
        adds=id_dish.adds_amount
        for a in toppings:
            topp_list.append(a.topping)
        data={
        'size':size,
        'adds':adds,
        'toppings':topp_list,
        }
        js = json.dumps({'size':size,
        'adds':adds,
        'toppings':topp_list,
        })
        return HttpResponse(js, content_type="application/json")

#function to show all clients orders
def show_order(request):
    if request.method=='GET':
        summ=0
        orderss=order.objects.filter(user=request.user, status="marked")
        confirmed=order.objects.filter(user=request.user, status="ordered")|order.objects.filter(user=request.user, status="done")
        for o in orderss:
            summ+=float(o.price)
        context = {
        "list_order":orderss,
        "price":summ,
        "confirmed":confirmed
        }
        return render(request, "orders/client_order.html", context)
    if request.method=='POST':
        orderss=order.objects.filter(user=request.user, status="marked")
        orderss.status="ordered"
        order.save()
        return render(request,"orders/error.html", {"error":"your order confirmed"} )

#function for deleting one of user orders
def del_order(request, id_dish):

    
    order.objects.filter(pk=id_dish, user=request.user, status="marked").delete()
    
    
       
        
    return redirect('show')

def confirm_order(request):
    orderss=order.objects.filter(user=request.user, status="marked")
    orderss.update(status="ordered")
    
    return render(request,"orders/error.html", {"error":"your order confirmed"} )
#function for view on users orders
def config_orders(request):
    a="john"
    if request.user.username==a:
        not_confirmed=order.objects.filter(status="marked")
        confirmed=order.objects.filter(status="ordered")
        done=order.objects.filter(status="done")
        context={
        'not_confirmed':not_confirmed,
        'confirmed':confirmed,
        'done':done
        }
        return render(request, 'orders/config.html', context)
    print(request.user)
    return redirect('index')
def done(request, id_dish):
    d=order.objects.get(pk=id_dish)
    d.status="done"
    d.save()
    return redirect('config')