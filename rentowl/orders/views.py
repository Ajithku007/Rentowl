from django.contrib import messages

from orders.models import Order

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from listings.models import Products
from datetime import datetime
from django.db.models import Q



# Create your views here.
#/

class bookingorder(View):
    def post(self, request, i):
        if not request.user.is_authenticated:
            messages.warning(request, "Please login or register to send a booking request.")
            return redirect("listings:productview", i)

        product = get_object_or_404(Products, id=i)

        date_range = request.POST.get("date_range")
        print("DATE RANGE:", date_range)

        if not date_range or " to " not in date_range:
            return redirect("listings:productview", i)

        start_date, end_date = date_range.split(" to ")
        start=datetime.strptime(start_date,"%Y-%m-%d").date()
        end=datetime.strptime(end_date,"%Y-%m-%d").date()

        conflict_booking=Order.objects.filter(product=product,status__in=['active','accepted'],
                                              start_date__lte=end,end_date__gte=start).exists()


        if conflict_booking:
            messages.error(request,"product already booked for selected dates")
            return redirect("listings:productview", i)

        Order.objects.create(
            product=product,
            borrower=request.user,
            start_date=start_date,
            end_date=end_date
        )

        return redirect("listings:productview", i)

