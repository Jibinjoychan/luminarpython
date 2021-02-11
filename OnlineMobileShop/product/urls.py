"""OnlineMobileShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings
from product.views import createBrand,delete,brandedit,brandview,createMobile,index,mobileView,deleteMobile,mobileViewDetails,mobileedit,order,viewOrders,orderDetails,register,loginPage,logOut,cancelOrder,adminviewoders



urlpatterns = [
    path('createbrand',createBrand,name="brandcreate"),
    path('delete/<int:pk>',delete,name='delete'),
    path('brandedit/<int:pk>',brandedit,name='brandedit'),
    path('brandview/<int:pk>',brandview,name='brandview'),
    path('createMobile',createMobile,name='createMobile'),
    path('',index,name='index'),
    path('mobileView/<int:pk>',mobileView,name='mobileView'),
    path('deleteMobile/<int:pk>',deleteMobile,name='deleteMobile'),
    path('mobileViewDetails/<int:pk>',mobileViewDetails,name='mobileViewDetails'),
    path('mobileedit/<int:pk>',mobileedit,name='mobileedit'),
    path('order/<int:pk>',order,name='order'),
    path('vieworder',viewOrders,name='viewOrder'),
    path('orderDetails/<int:pk>',orderDetails,name='orderDetails'),
    path('register',register,name='register'),
    path("",lambda request:render(request,"product/base.html")),
    path("logoutpage",logOut,name='logoutpage'),
    path("cancelOrder",cancelOrder,name='cancelOrder'),
    path("adminvieworders",adminviewoders,name='adminvieworders')

]

