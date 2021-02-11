from django.shortcuts import render,redirect
from product.forms import BrandCreateForm,BrandEditForm,MobileCreateFrm,MobileEditFrm,OrderFrm,OrderUpdateFrm,SearchForm,RegistrationForm
from product.models import Brand,Mobile,Orders
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def createBrand(request):

    form=BrandCreateForm()
    context={}
    context["form"]=form
    qs = Brand.objects.all()
    context["brands"] = qs
    if request.method=='POST':
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("brandcreate")
    return render(request,"product/createBrand.html",context)

def delete(request,pk):
    entry=Brand.objects.get(id=pk)
    entry.delete()
    form = BrandCreateForm()
    context = {}
    context["form"] = form
    qs = Brand.objects.all()
    context["brands"] = qs
    return render(request,"product/createBrand.html",context)

def brandedit(request,pk):
    obj = Brand.objects.get(id=pk)
    form=BrandEditForm(instance=obj)
    context={}
    context["form"]=form
    if (request.method=="POST"):
        print(pk)
        form=BrandEditForm(request.POST)
        obj = Brand.objects.get(id=pk)
        form=BrandEditForm(instance=obj,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("brandcreate")
        else:
            context={}
            context["form"]=BrandEditForm(request.POST)
            return render(request, "product/editbrand.html", context)
    return render(request,"product/editbrand.html",context)

def brandview(request,pk):
    obj = Brand.objects.get(id=pk)
    form=BrandCreateForm(instance=obj)
    context={}
    context["form"]=form
    return render(request,"product/viewbrand.html",context)

def createMobile(request):
    form=MobileCreateFrm()
    context={}
    context['form']=form
    mobiles=Mobile.objects.all()
    context["mobiles"]=mobiles
    if(request.method=="POST"):
        form=MobileCreateFrm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("createMobile")
    return render(request,"product/createMobile.html",context)

@login_required(login_url='loginPage')
def index(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    form=SearchForm()
    context["search"]=form
    if request.method=="POST":
        form=SearchForm(request.POST)
        if form.is_valid():
            brand=form.cleaned_data.get("Brand_name")
            products=Mobile.objects.filter(brand__brand_name=brand)
            context["mobiles"]=products
            return render(request,"product/index.html", context)

    return render(request,"product/index.html",context)

def mobileView(request,pk):
    obj=Mobile.objects.get(id=pk)
    context={}
    context["mobile"]=obj
    return render(request,"product/itemView.html",context)

def deleteMobile(request,pk):
    entry=Mobile.objects.get(id=pk)
    entry.delete()
    form = MobileCreateFrm()
    context ={}
    context["form"] = form
    qs = Mobile.objects.all()
    context["mobile"] = qs
    return render(request,"product/createMobile.html",context)

def mobileViewDetails(request,pk):
    obj=Mobile.objects.get(id=pk)
    context={}
    context["mobile"]=obj
    return render(request,"product/itemView.html",context)

def mobileedit(request,pk):
    obj = Mobile.objects.get(id=pk)
    form=MobileEditFrm(instance=obj)
    context={}
    context["form"]=form
    if (request.method=="POST"):
        print(pk)
        form=MobileEditFrm(request.POST,request.FILES)
        obj = Mobile.objects.get(id=pk)
        form=MobileEditFrm(instance=obj,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createMobile")
        else:
            context={}
            context["form"]=BrandEditForm(request.POST)
            return render(request, "product/editmobile.html", context)
    return render(request,"product/editmobile.html",context)


def order(request,pk):
    context={}
    form=OrderFrm(initial={'productid':pk,"user":request.user})
    context["form"]=form
    if request.method=='POST':
        form=OrderFrm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"product/sucess.html")
    return render(request,"product/purchase.html",context)


def viewOrders(request):
    qs=Orders.objects.filter(user=request.user).filter(active_status=1)
    context={}
    context["qs"]=qs
    return render(request,"product/vieworders.html",context)

def orderDetails(request,pk):
    qs=Orders.objects.get(id=pk)
    product=qs.productid
    item=Mobile.objects.get(id=product)
    form=OrderUpdateFrm(instance=qs)
    context={}
    context["form"]=form
    context["item"]=item
    if request.method=="POST":
        form=OrderFrm(instance=qs,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewOrder")
    return render(request,"product/orderdetails.html",context)

def searchproduct(request):

    return render(request,"product/index.html")

def register(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        print("inside post")
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginPage")
        else:
            context["form"]=form
            return render(request, "product/registration.html", context)
    return render(request,"product/registration.html",context)

def loginPage(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password = request.POST.get("pwd")
        print(username,",",password)
        if((username=="admin")&(password=="admin")):
            return render(request,"product/adminbase.html")
        else:

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("index")
            else:
                return redirect("loginPage")
    return render(request,"product/login.html")

def logOut(request):
    logout(request)
    return redirect("loginPage")

def cancelOrder(request,pk):
    order=Orders.objects.get(id=pk)
    order.active_status=0
    order.save()
    return render(request,"product/index.html")


def adminviewoders(request):
    qs = Orders.objects.all()
    context = {}
    context["qs"] = qs
    return render(request, "product/adminvieworders.html", context)


