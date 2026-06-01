"""
URL configuration for rentowl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from dashboard import views



app_name='dashboard'
urlpatterns = [
path('dashboard/',views.Dashboardview.as_view(),name='dashboard'),
path("order/<int:order_id>/update/", views.UpdateOrderStatusView.as_view(), name="update_order_status"),
    path('Editprofile/',views.Editprofile.as_view(),name="editprofile"),
    path('OrderDetail/<int:pk>/',views.Order_detail.as_view(),name="Orderdetail"),
    path('Products_listed/',views.listed_products.as_view(),name="listedproducts"),
    path('Editproduct/<int:pk>/',views.EditProductView.as_view(),name='editproduct'),
    path('DeleteProduct/<int:pk>/',views.DeleteProduct.as_view(),name='Deleteproduct')
]
