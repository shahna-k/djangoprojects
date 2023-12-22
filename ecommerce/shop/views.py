from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from shop.models import Category,Product
from django.contrib.auth.decorators import login_required

def allcategories(request):
    c=Category.objects.all()
    return render(request,'categories.html',{'c':c})


def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})


def details(request,d):
    p=Product.objects.get(name=d)
    d=Product.objects.filter(name=p)
    return render(request,'details.html',{'p':p,'d':d})

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        if(p==cp):
            u = User.objects.create_user(username=u, password=p, email=e)
            u.save()
            return redirect('shop:login')
        else:
            return HttpResponse("Password not matching")
    return render(request,'register.html')

def user_login(request):
    if (request.method == "POST"):
        name = request.POST['n']
        pass1 = request.POST['p']
        user = authenticate(username=name, password=pass1)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)