from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import  View
from accounts.forms import Registerform,Loginform
from django.contrib import messages
from listings.models import Products
# Create your views here.
#---- home page----
class Homepage(View):
    def get(self,request):
        loginform_instance = Loginform()
        Registerform_instance=Registerform()
        products=Products.objects.all().order_by('-created_at')[:6]
        context={'loginform':loginform_instance,'registerform':Registerform_instance,'recent_products':products}
        return render(request,'base.html',context)

#---- admin page -----
class Adminpage(View):
    def get(self,request):
        return render(request,'admin.html')


#----  register ------
class Register(View):
    def post(self,request):
        form_instance=Registerform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('accounts:homepage')
        loginform_instance=Loginform()
        form_instance=Registerform()
        context = {
            'loginform': loginform_instance,
            'registerform': form_instance,
        }
        return render(request,'base.html',context)

class Userlogin(View):

    def post(self,request):
        loginform_instance=Loginform(request.POST)
        print(loginform_instance.errors)
        if loginform_instance.is_valid():
            u=loginform_instance.cleaned_data['username']
            p=loginform_instance.cleaned_data['password']
            user=authenticate(request,username=u,password=p)
            if user :
                login(request, user)
                if user.is_superuser:
                    return redirect('accounts:adminpage')
                else:
                    return redirect('accounts:homepage')
            else:
                messages.error(request, "invalid credentials")
                return redirect('accounts:homepage')


class Userlogout(View):
    def get(self,request):
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect('accounts:homepage')

from django.contrib.auth import  get_user_model
user=get_user_model()

u=user.objects.get(username="gus")
print(u.profile_image)


