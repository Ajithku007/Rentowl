from itertools import product

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from orders.models import Order


# Create your views here.
# class Dashboardview(View):
#     def get(self,request):
#         orders=Order.objects.filter(borrower=request.user)
#         context={'order':orders}
#         return render(request,'dashboard.html',context)

from django.shortcuts import render
from dashboard.forms import Editprofileform

class Dashboardview(View):
    def get(self, request):
        my_orders = Order.objects.filter(borrower=request.user)
        received_orders=Order.objects.filter(product__owner=request.user)

        context = {
            "my_orders": my_orders,
            "received_orders":received_orders,
            "total_orders": my_orders.count(),
            "active_orders": my_orders.filter(status="approved").count(),
            "completed_orders": my_orders.filter(status="completed").count(),
            "orders":received_orders.count(),
            "active_rentals":received_orders.filter(status='approved').count(),
            "completed_rentals":received_orders.filter(status='completed').count()
        }
        return render(request, "dashboard.html", context)


class UpdateOrderStatusView( View):
    def post(self, request, order_id):
        order = get_object_or_404(
            Order,
            id=order_id,
            product__owner=request.user   #  owner-only access
        )

        action = request.POST.get("action")

        if action == "approve":
            order.status = "approved"
        elif action == "reject":
            order.status = "rejected"

        order.save()
        return redirect('dashboard:dashboard')


class Editprofile(View):
    def get(self,request):
        user=request.user
        form_instance=Editprofileform(instance=user)
        context={'form':form_instance}
        return render(request,'editprofile.html',context)
    def post(self,request):
        user = request.user
        form_instance=Editprofileform(request.POST,request.FILES,instance=user)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('dashboard:dashboard')



# ----- order detail-------
class Order_detail(View):
    def get(self,request,pk):
        order=get_object_or_404(Order,id=pk)
        return render(request,'order_detail.html',{'order':order})


#     ----- user's listed products---
from listings.models import Products
class listed_products(View):
    def get(self,request):
        products=Products.objects.filter(owner=request.user)
        return render(request,'user_products.html',{'products':products})



from listings.forms import Productform
# edit listed product
class EditProductView(View):
    def get(self, request, pk):
        product = Products.objects.get(id=pk)
        form = Productform(instance=product)
        return render(request, "edit_product.html", {"form": form})

    def post(self, request, pk):
        product = Products.objects.get(id=pk)
        form = Productform(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect("dashboard:my-products")

        return render(request, "edit_product.html", {"form": form})


# delete listed product
class DeleteProduct(View):
    def get(self,request,pk):
        product=get_object_or_404(Products,id=pk)
        if product.owner==request.user:
         product.delete()
        return redirect('dashboard:listedproducts')