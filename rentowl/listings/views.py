from django.http import JsonResponse
from datetime import  datetime
from django.shortcuts import render, redirect
from django.views import View
from listings.forms import Productform
from listings.models import Category,Products
from django.db.models import Q
# Create your views here.
from django.views import View

from orders.models import Order


class Shopview(View):
    def get(self,request):
        return render(request,'shop.html')


class addProduct(View):
    def get(self,request):
        form_instance=Productform()
        context={'form':form_instance}
        return render(request,'addproduct.html',context)
    def post(self,request):
        form_instance=Productform(request.POST,request.FILES)
        if form_instance.is_valid():
            product=form_instance.save(commit=False)
            product.owner=request.user
            product.save()
            return redirect('accounts:homepage')
        return render(request,'addproduct.html',{'form':form_instance})

class ListingsView(View):
    def get(self,request):
        category=Category.objects.all()
        products=Products.objects.all()
        context={'category':category,'products':products}
        return render(request,'listings.html',context)

class Productview(View):
    def get(self,request,i):
        p=Products.objects.get(id=i)

        if request.user.is_authenticated:
            user_order=Order.objects.filter(product=p,borrower=request.user).order_by("-created_at").first()
        else:
            user_order=None

        # ajax price calculation
        if request.headers.get("x-requested-with") == "XMLHttpRequest"  :   #checks if the request is an ajax request
            start_date=request.GET.get("start_date")
            end_date=request.GET.get("end_date")

            if not (start_date and end_date):
                return JsonResponse({'error':'missing_dates'},status=400)

            start=datetime.strptime(start_date,"%Y-%m-%d").date()
            end=datetime.strptime(end_date,"%Y-%m-%d").date()

            days=(end-start).days+1
            total_price=p.rent_price * days

            return JsonResponse({'price':total_price})
        context={'product':p,'user_order':user_order}
        return render(request,'productview.html',context)


class Searchview(View):
    def get(self,request):
        query=request.GET['q']
        if query:
         products=Products.objects.filter(Q(title__icontains=query)|Q(category__category_name__icontains=query)|
                                         Q(rent_price__icontains=query)|Q(description__icontains=query)|
                                         Q(location__icontains=query))

        context={'products':products,'query':query}
        return render(request,'searchview.html',context)

