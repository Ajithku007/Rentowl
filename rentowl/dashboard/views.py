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